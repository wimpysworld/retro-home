#!/usr/bin/env python3

import os
import psutil
import setproctitle
import signal
import subprocess
import sys
import time
from gpiozero import Button, LED
from subprocess import DEVNULL


def process_kill(process_name: str):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.kill()


def button_dispatch(cmd: str):
    print(cmd)
    if cmd == 'poweroff' or cmd == 'reboot':
        led.blink(0.25, 0.25)
        # Sleep for a moment to allow the blinking LED to be observed
        time.sleep(1)
        process_kill('ludo')
        subprocess.Popen([cmd], stdout=DEVNULL, stderr=DEVNULL)
    else:
        print('Unknown command: ' + cmd)


# Signal handler that exits gracefully
def signal_handler(signal_received, frame):
    sys.exit(0)


if __name__ == "__main__":
    status = None

    setproctitle.setproctitle('retroflag-safeshutdown')

    # Initialise the signal handler to catch Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    POWER_PIN = 4
    POWER_SWITCH = 3
    RESET_SWITCH = 2
    LED_PIN = 14

    # This is the case LED.
    led = LED(LED_PIN)
    led.on()

    # This is not a LED. It is used as power control.
    power = LED(POWER_PIN)
    power.on()

    power_button = Button(POWER_SWITCH)
    reset_button = Button(RESET_SWITCH)

    # Loop forever looking for button presses
    while status is None:
        if reset_button.is_pressed:
            status = 'reboot'
        elif power_button.is_pressed:
            status = 'poweroff'
        else:
            time.sleep(0.5)

    # https://github.com/gpiozero/gpiozero/issues/707
    # GPIOZero has an implicit clean up that returns pins to the values they
    # initially had.

    # This causes the system to reset or power off immediately, when this script
    # exits. Meaning is it going to be tricky to mark that a safe power off is
    # requested and handle that via the another systemd unit in the final.target.

    button_dispatch(status)
    if status == 'poweroff':
        # 🐷 meets 💄 here

        # Best efforts to sync all buffers to disk
        # If power.off() is not called the fans will keep running after the Pi
        # is powered down and the power switch will not power be able to power
        # on the device again.
        os.sync()

        # I really want to sleep or assess power off progress, but anything
        # significant added here fails to deliver the power.off() signal that
        # follows.
        #time.sleep(0.1)

        # Wham! 🥊 Good night sweet prince 😵
        power.off()
    else:
        # Keep this process alive until the system reboots. At least reboots are
        # graceful.
        signal.pause()

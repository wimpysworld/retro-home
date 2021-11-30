#!/usr/bin/env python3

import RPi.GPIO as GPIO
import psutil
import time
import os

POWER = 3
RESET = 4


def process_kill(process_name: str):
	for process in psutil.process_iter():
		if process.name() == process_name:
			process.kill()


if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(POWER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	while True:
		if (GPIO.input(RESET) == False):
			process_kill("ludo")
			os.system("reboot")
			break
		elif (GPIO.input(POWER) == False):
			process_kill("ludo")
			os.system("poweroff")
			break
		time.sleep(0.50)

#!/usr/bin/env python3

import psutil
import subprocess
import time

from gpiozero import Button
from subprocess import DEVNULL

POWER = 3
RESET = 4


def process_kill(process_name: str):
	for process in psutil.process_iter():
		if process.name() == process_name:
			process.kill()


if __name__ == "__main__":
	power_button = Button(POWER)
	reset_button = Button(RESET)

	while True:
		if reset_button.is_pressed:
			process_kill("ludo")
			subprocess.Popen(['reboot'], stdout=DEVNULL, stderr=DEVNULL)
			break
		elif power_button.is_pressed:
			process_kill("ludo")
			subprocess.Popen(['poweroff'], stdout=DEVNULL, stderr=DEVNULL)
			break
		time.sleep(0.50)

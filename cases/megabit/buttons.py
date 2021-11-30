#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os

POWER = 3
RESET = 4

if __name__ == "__main__":

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(POWER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	while True:
		if (GPIO.input(RESET) == False):
			os.system("reboot")
			break
		elif (GPIO.input(POWER) == False):
			os.system("poweroff")
			break
		time.sleep(0.50)

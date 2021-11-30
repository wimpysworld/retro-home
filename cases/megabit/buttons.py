#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os

power = 3
reset = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(power, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO.input(reset) == False):
		os.system("sudo reboot -h now")
		break
	elif (GPIO.input(power) == False):
		os.system("sudo shutdown -h now")
		break
	time.sleep(0.50)

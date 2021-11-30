#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO.input(3) == False):
		os.system("sudo shutdown -h now")
		break
	time.sleep(0.50)

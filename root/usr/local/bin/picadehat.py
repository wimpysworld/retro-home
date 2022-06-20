#!/usr/bin/env python3

## https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html
## https://github.com/pimoroni/picade-hat/blob/master/legacy-python-driver/gamepads/picadehat-default
## https://gpiozero.readthedocs.io/en/stable/api_boards.html#buttonboard
from gpiozero import Device, LED, ButtonBoard, Button
## This can be commented out after tests
from gpiozero.pins.mock import MockFactory, MockPWMPin
import os
import time
import sys
from signal import pause

## This is only for test purpose
Device.pin_factory = MockFactory(pin_class=MockPWMPin)

try:
    from evdev import uinput, UInput, ecodes as e
except ImportError:
    exit("This library requires the evdev module\nInstall with: sudo pip install evdev")


BOUNCE_TIME = 0.01 # Debounce time in seconds
SHUTDOWN_HOLD_TIME = 3 # Time in seconds that power button must be held

SHUTDOWN = 4
BUTTON_POWER = 17
VOLUME_DOWN = 13
VOLUME_UP = 26

UP = 12
DOWN = 6
LEFT = 20
RIGHT = 16

BUTTON1 = 5
BUTTON2 = 11
BUTTON3 = 8
BUTTON4 = 25
BUTTON5 = 9
BUTTON6 = 10

ENTER = 27
ESCAPE = 22
COIN = 23
START= 24

buttons = ButtonBoard(UP, DOWN, LEFT, RIGHT, BUTTON1, BUTTON2, BUTTON3, BUTTON4, BUTTON5, BUTTON6, ENTER, ESCAPE, COIN, START, bounce_time=BOUNCE_TIME)

KEYS = {
    ENTER: e.KEY_ENTER,
    ESCAPE: e.KEY_ESC,
    COIN: e.KEY_C,
    START: e.KEY_S,
    UP: e.KEY_UP,
    DOWN: e.KEY_DOWN,
    LEFT: e.KEY_LEFT,
    RIGHT: e.KEY_RIGHT,
    BUTTON1: e.KEY_LEFTCTRL,
    BUTTON2: e.KEY_LEFTALT,
    BUTTON3: e.KEY_SPACE,
    BUTTON4: e.KEY_LEFTSHIFT,
    BUTTON5: e.KEY_Z,
    BUTTON6: e.KEY_X
}

## UDEV rule need for user to work with Uinput
try:
    ui = UInput({e.EV_KEY: KEYS.values()}, name="Picade-HAT", bustype=e.BUS_USB)

except uinput.UInputError as e:
    sys.stdout.write(e.message)
    sys.stdout.write("Have you tried running as root? sudo {}".format(sys.argv[0]))
    sys.exit(0)

print(buttons.is_pressed)
pause()
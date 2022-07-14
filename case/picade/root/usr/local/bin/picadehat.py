#!/usr/bin/env python3

## This is meant to refactor the whole process of getting the gamepad to work
## only with just defining Object it should initialize the gamepad and start the main loop
from gpiozero import LED, Button
import os
from time import sleep
import sys
from signal import pause

## These two lines can be commented out when testing on real hardware
#from gpiozero import Device
#from gpiozero.pins.mock import MockFactory, MockPWMPin
#Device.pin_factory = MockFactory(pin_class=MockPWMPin)
#warnings.simplefilter('ignore')

try:
    from evdev import uinput, UInput, ecodes as e
except ImportError:
    exit("This library requires the evdev module\nInstall with: sudo pip install evdev")


class Action:
    def __init__(self,name, pin, purpose="button", bounce=0.01, keycode=None, press_command=None, release_command=None, held_time=None, held_action=None, pull_up=True):
        self.name = name
        self.pin = pin
        self.purpose = purpose
        self.keycode = keycode
        self.bounce = bounce
        self.held_time = held_time
        self.held_action = held_action
        self.pull_up = pull_up
        if self.purpose == "button" and self.keycode is not None:
            self.press_command = lambda x=self.keycode : [ui.write(e.EV_KEY, x, 1),ui.syn()]
            self.release_command = lambda x=self.keycode : [ui.write(e.EV_KEY, x, 0),ui.syn()]
        elif self.purpose == "button" and self.keycode is None:
            self.press_command = press_command
            self.release_command = release_command

        match self.purpose:
            case "button":
                    self.obj = Button(self.pin, pull_up=self.pull_up, bounce_time=self.bounce)
                    self.obj.when_pressed = self.press_command
                    self.obj.when_released = self.release_command
        
            case "function_key":
                self.obj = Button(self.pin, pull_up=self.pull_up, bounce_time=self.bounce, hold_time=self.held_time)
                self.obj.when_held = self.held_action
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
        
    def shutdown():
        os.system("shutdown -h now")



if __name__ == "__main__":
    #HAD to define keycodes first before defining the gamepad, so that we could init our virtual gamepad with capabilites set
    #CHANGE
    KEYS = {
        "VOLUME_UP": e.KEY_VOLUMEUP,
        "VOLUME_DOWN": e.KEY_VOLUMEDOWN,
        "UP": e.KEY_UP,
        "DOWN": e.KEY_DOWN,
        "LEFT": e.KEY_LEFT,
        "RIGHT": e.KEY_RIGHT,
        "SELECT": e.BTN_SELECT,
        "START": e.BTN_START,
        "COIN": e.BTN_THUMBL,
        "ESCAPE": e.KEY_ESC,
        "SELECT": e.BTN_SELECT,
        "BUTTON_1": e.BTN_A,
        "BUTTON_2": e.BTN_X,
        "BUTTON_3": e.BTN_TR,
        "BUTTON_4": e.BTN_B,
        "BUTTON_5": e.BTN_Y,
        "BUTTON_6": e.BTN_TL
    }

    ## for this to work you need udev rule to allow access to the uinput device to be created, and uinput kernel module to be loaded 
    ## this is done in the following way:
    ## create /etc/udev/rules.d/99-uinput.rules
    ## add the following line:
    ## SUBSYSTEM=="misc", KERNEL=="uinput", MODE="0660", GROUP="ludo"

    try:
        ui = UInput({e.EV_KEY: KEYS.values()}, name="Picade-HAT", bustype=e.BUS_USB)
    except uinput.UInputError as e:
        sys.stdout.write(e.message)
        sys.stdout.write("You don't have permission to create the uinput device or kernel module not loaded.\n")
        sys.exit(0)

    #define gpio buttons
    #CHANGE
    btn_volup =  Action("VolumeUP", pin=26, keycode=KEYS["VOLUME_UP"])
    btn_voldown = Action("VolumeDOWN", pin=13, keycode=KEYS["VOLUME_DOWN"])
    btn_up = Action("UP", pin=12, keycode=KEYS["UP"]) 
    btn_down = Action("DOWN", pin=6, keycode=KEYS["DOWN"]) 
    btn_left = Action("LEFT", pin=20, keycode=KEYS["LEFT"])
    btn_right = Action("RIGHT", pin=16, keycode=KEYS["RIGHT"])
    btn_but1 = Action("BUTTON1", pin=5, keycode=KEYS["BUTTON_1"]) 
    btn_but2 = Action("BUTTON2", pin=11, keycode=KEYS["BUTTON_2"]) 
    btn_but3 = Action("BUTTON3", pin=8, keycode=KEYS["BUTTON_3"]) 
    btn_but4 = Action("BUTTON4", pin=25, keycode=KEYS["BUTTON_4"]) 
    btn_but5 = Action("BUTTON5", pin=9, keycode=KEYS["BUTTON_5"]) 
    btn_but6 = Action("BUTTON6", pin=10, keycode=KEYS["BUTTON_6"]) 
    btn_start = Action("START", pin=24, keycode=KEYS["START"]) 
    btn_select = Action("SELECT", pin=27, keycode=KEYS["SELECT"]) 
    btn_coin = Action("COIN", pin=23, keycode=KEYS["COIN"]) 
    btn_esc = Action("ESCAPE", pin=22, keycode=KEYS["ESCAPE"]) 
    btn_power = Action("Power_Button", 17, purpose="function_key", held_time=3, held_action=shutdown) 

    ###test with mock pins changing pin state
#    while True:
#        print(btn_esc.name)
#        btn_esc.obj.pin.drive_low()
#        sleep(4)
#        btn_esc.obj.pin.drive_high()
#        print(f'button state: {btn_esc.obj.value}')
#        sleep(2)
     ### Testing just evdev
     ### evdev device won't appear as input until the first keycode injected.
#    while True:
#        ui.write(e.EV_KEY, e.BTN_START, 1)
#        sleep(5)
#        ui.write(e.EV_KEY, e.BTN_START, 0)
#        ui.syn()
    # close evdev device
    ui.close()
    # wait for signal
    pause()
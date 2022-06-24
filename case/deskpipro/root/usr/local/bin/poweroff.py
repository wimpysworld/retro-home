#!/usr/bin/env python3
# This script will sends 'power_off' to DeskPi Pro MCU. After 8 seconds the
# daughter board will cut all power to the Raspberry Pi.

# Send commands to the MCU via QinHeng Electronics CH340 serial converter
#   - pwm_xxx:   represents fan speed from 000 to 100; 050 = 50%
#   - power_off: sends the power off signal which will cut power after 8 seconds


import serial
import sys


if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyCH340", 9600, timeout=30)
    try:
        if ser.isOpen():
            ser.write(b'pwm_000')
            ser.write(b'power_off')
            ser.close()
    except:
        if ser.isOpen():
            ser.close()

    sys.exit()

#!/usr/bin/env python3
# Monitor the CPU temperature and adjust DeskPi Pro fan speed accordingly.

# Send commands to the MCU via QinHeng Electronics CH340 serial converter
#   - pwm_xxx:   represents fan speed from 000 to 100; 050 = 50%


from time import sleep
import serial
import sys


def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = int(f.read()) / 1000.0
    return int(temp)


if __name__ == '__main__':
    while True:
        try:
            ser = serial.Serial("/dev/ttyCH340", 9600, timeout=30)
            if ser.isOpen():
                cpu_temp = get_cpu_temperature()
                #print(cpu_temp)

                if cpu_temp > 80:
                    ser.write(b'pwm_100')
                elif cpu_temp > 65:
                    ser.write(b'pwm_075')
                elif cpu_temp > 50:
                    ser.write(b'pwm_040')
                elif cpu_temp > 45:
                    ser.write(b'pwm_025')
                else:
                    ser.write(b'pwm_000')

            sleep(5)
        except KeyboardInterrupt:
            if ser.isOpen():
                ser.close()
            sys.exit()

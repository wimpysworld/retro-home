#!/usr/bin/env python3
# Monitor the CPU temperature and adjust DeskPi Pro fan speed accordingly.

# Send commands to the MCU via QinHeng Electronics CH340 serial converter
#   - pwm_xxx:   represents fan speed from 000 to 100; 050 = 50%


from time import sleep
import serial
import setproctitle
import signal
import sys

# Reads the CPU temp and returns an int
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = int(f.read()) / 1000.0
    return int(temp)


# Signal handler that exits gracefully
def signal_handler(signal_received, frame):
    sys.exit(0)


if __name__ == '__main__':
    setproctitle.setproctitle('deskpipro-fancontrol')

    # Initialise the signal handler to catch Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        ser = serial.Serial("/dev/ttyCH340", 9600, timeout=30)
        cpu_temp = get_cpu_temperature()
        if ser.isOpen():
            if cpu_temp > 80:
                fan_speed = '100'
            elif cpu_temp > 65:
                fan_speed = '75'
            elif cpu_temp > 50:
                fan_speed = '40'
            elif cpu_temp > 45:
                fan_speed = '25'
            else:
                fan_speed = '0'
            print(f"CPU: {cpu_temp}°C\tFAN: {fan_speed}%")

            pwm_data = 'pwm_' + fan_speed.zfill(3)
            ser.write(pwm_data.encode('utf-8'))
            ser.close()
        else:
            print('Could not connect to /dev/ttyCH340')
        sleep(5)

#!/usr/bin/env python3
import evdev
from time import sleep

dev = None
while dev is None:
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        #print(device.path, device.name, device.phys)
        if device.name == "Picade-HAT":
            print(f"Found Picade-HAT on {device.path}")
            dev = evdev.InputDevice(device.path)
            break
        else:
            continue
    if dev is None:
        print("Could not find Picade-HAT, retrying...")
        sleep(2)

print(dev)
print(dev.capabilities(verbose=True))
for event in dev.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
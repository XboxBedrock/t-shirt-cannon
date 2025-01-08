import evdev
import sys
import time
import util

controller_name = "Xbox Wireless Controller"

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

found_path = None

for device in devices:
    if device.name == controller_name:
        found_path = device.path
        
if found_path == None:
    print("Controller not found, check name")
    sys.exit()
    
controller = evdev.InputDevice(found_path)
print(controller.capabilities(verbose=True, absinfo=True))
#read events
while True:
    print(util.clean_input_127(controller.absinfo(evdev.ecodes.ABS_X)))
    print(controller.active_keys(verbose=True))
    time.sleep(0.5)
import evdev
import sys
import time
import util
import RPi.GPIO as gpio

lport = 2
rport = 3

#gpio init stuff
gpio.setmode(gpio.BCM)
gpio.setup(lport, gpio.OUT)
gpio.setup(rport, gpio.OUT)

#50hz standard
lpwm = gpio.PWM(lport ,50)
rpwm = gpio.PWM(rport, 50)

#neutral position
lpwm.start(50)
rpwm.start(50)


controller_name = "Xbox Wireless Controller"
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

found_path = None

for device in devices:
    print(device.name)
    if device.name == controller_name:
        found_path = device.path
        
if found_path == None:
    print("Controller not found, check name")
    sys.exit()
    
controller = evdev.InputDevice(found_path)
print(controller.capabilities(verbose=True, absinfo=True))
#read events
while True:
    x_val = util.clean_input_127(controller.absinfo(evdev.ecodes.ABS_X))
    y_val = util.clean_input_127(controller.absinfo(evdev.ecodes.ABS_Y))
    left = y_val - x_val
    right = y_val + x_val
    rpwm.ChangeDutyCycle(util.pwm_ify(right))
    lpwm.ChangeDutyCycle(util.pwm_ify(left))
    print(util.is_button_pressed('A', controller))
    time.sleep(0.5)
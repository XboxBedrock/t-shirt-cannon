import evdev

button_maps = {
    307: "X",
    308: "Y",
    304: "A",
    305: "B"
    }

def pwm_ify(val: int):
    val = min(val, 127)
    val = max(val, -127)
    val += 127
    val *= 100/254
    return int(val)

#clean the reading and scale to -127 to +127
def clean_input_127(device_reading: evdev.device.AbsInfo):
    if abs(device_reading.value) < device_reading.flat:
        return 0
    
    val = max(device_reading.value, device_reading.min)
    val = min(val, device_reading.max)
    
    #assume uniform scale
    val *= 127/abs(device_reading.min)
    
    return int(val) if (val < 0) else int(val+0.5)

def is_button_pressed(name: str, device: evdev.InputDevice):
    pressed = [button_maps.get(i) for i in device.active_keys()]
    return name in pressed
    
    
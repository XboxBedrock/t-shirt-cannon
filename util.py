import evdev

#clean the reading and scale to -127 to +127
def clean_input_127(device_reading: evdev.device.AbsInfo):
    if abs(device_reading.value) < device_reading.flat:
        return 0
    
    val = max(device_reading.value, device_reading.min)
    val = min(val, device_reading.max)
    
    #assume uniform scale
    val *= 127/abs(device_reading.min)
    
    return int(val) if (val < 0) else int(val+0.5)
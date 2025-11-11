# T-Shirt Cannon

<img src="cannon.jpeg" height="500">

Hi! If you're reading this, you've come across the code for the Cal High Robotics T-Shirt cannon. You can check some of the mechanical design out on [my blog](https://blog.sushrut.dev) (part 2 coming soon).

The code is split between `main.py` and `util.py`, written to target a Raspberry Pi. The XPadNeo driver is used to connect with an Xbox Controller, using evdev to read input.

Features of this program: 
- Arcade drive with drive curves and deadzoning
- Button-activated relays for solenoids and horns
- Cruise control
- Controller search and re-connect logic
- Winch control

The Pi has a cron job that starts the program on boot, for a hands-free startup sequence.

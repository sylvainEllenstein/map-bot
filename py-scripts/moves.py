# File that manages connection with robot using bluedot and gpiozero, and allows to control manually the movement 
# This is only an API for facilitating communication with servos and motors

from bluedot import *
from gpiozero import *
from signal import pause
from time import *
from adafruit_servokit import * # only using ServoKit ?

kit = ServoKit(channels=16)

# funcs : kit.servo[i].angle = n 
#         kit.servo[i].actuation_range = n
#         kit.servo[i].set_pulse_widht_range(min = 1000, max = 2000)
#         kit.continuous_servo[i].throttle = j (max 1, min 0)
# i is the channel the servo is connected to
 
"""
Config : 

1 and 2 : Main continuous servo
3 and 4 : optional continuous servos

5 : main head-rotating servo (180°... --> precise, not heavy / powerful)
"""

def forward(boolFunc, speed=1):
	kit.continuous_servo[1].throttle = speed
	kit.continuous_servo[2].throttle = -speed
	# starting here a new thread would be nice...
	# then call a function that close both servos
	while boolFunc():
		pass
	kit.continuous_servo[1].throttle = kit.continuous_servo[2].throttle = 0
	

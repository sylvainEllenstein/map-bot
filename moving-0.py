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

**************
Mode of operation :
there are mutiple choices, but this is very important for the following functionnement of the bot...

takes as argument a bool : --> uses while, good if the motor can be free-running (no need to stop and re-start before each loop...)

takes as argument a timeout : will very probably function (no physical jitter) but will be less acccurate on moves, and can't stop moving at each moment



"""

def forward(boolF):
    pass

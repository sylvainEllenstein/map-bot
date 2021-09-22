# File that manages connection with robot using bluedot and gpiozero, and allows to control manually the movement 

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

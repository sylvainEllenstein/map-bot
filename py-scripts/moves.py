#!/usr/bin/python3

# File that manages connection with robot using bluedot and gpiozero, and allows to control manually the movement 
# This is only an API for facilitating communication with servos and motors

from gpiozero import *
from signal import pause
from time import *
import threading
# from adafruit_servokit import * # only using ServoKit ?
from adafruit_motorkit import MotorKit

# Other custom localisation scripts are to be imported ...
# funcs : kit.servo[i].angle = n 
#         kit.servo[i].actuation_range = n
#         kit.servo[i].set_pulse_widht_range(min = 1000, max = 2000)
#         kit.continuous_servo[i].throttle = j (max 1, min 0)
# i is the channel the servo is connected to
 
#------------------ CONSTANTS  ------------------------

l = 4.5 # corresponds to width/2 of vehicle
L = 15 # corresponds to length of vehicle
kit = ServoKit(channels=16) 
"""
Config : 

1 and 2 : Main continuous servo
3 and 4 : optional continuous servos

5 : main head-rotating servo (180°... --> precise, not heavy / powerful : --> tryong feedback servo would be great)
"""
#------------------  PHYSICAL PINS ATTRIBUTION ----------------

motors = MotorKit(0x40)
"""
# Forward at full throttle
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
# Right at half speed
kit.motor1.throttle = 0.5
kit.motor2.throttle = -0.5
"""


#------------------  MAIN CUSTOM CLASSES  ---------------------

class boolMoveThread(threading.Thread) :
	# This type of thread is to be created within a forward or backward function, and it lets run the main motors until a condition
	# becomes False (called by boolFunc); may be used within another type of function :
	# UPDATE : has to be recoded because of new DC motors but mstill remain interesting

#--------------  MAIN FUNCS  -----------------
		
def forward(boolFunc, speed=1):
	
	pass
	
def rotationMove(angle, radius, *args):
	# takes an angle + radius as argument, and turns with it on distance radius
	pass
	
	

#!/usr/bin/python3

# File that manages connection with robot using bluedot and gpiozero, and allows to control manually the movement 
# This is only an API for facilitating communication with servos and motors

import gpiozero
import time
import threading
from global_funcs import *

# from adafruit_servokit import * # only using ServoKit ?
from adafruit_motorkit import MotorKit

# Other custom localisation scripts are to be imported ...
# funcs : kit.servo[i].angle = n 
#         kit.servo[i].actuation_range = n
#         kit.servo[i].set_pulse_widht_range(min = 1000, max = 2000)
#         kit.continuous_servo[i].throttle = j (max 1, min 0)
# i is the channel the servo is connected to
 
#------------------ CONSTANTS  ------------------------


# kit = ServoKit(channels=16) 
"""
Config : 

1 and 2 : Main continuous servo
3 and 4 : optional continuous servos

5 : main head-rotating servo (180°... --> precise, not heavy / powerful : --> tryong feedback servo would be great)
"""
#------------------  PHYSICAL PINS ATTRIBUTION ----------------

motors = MotorKit(0x40)
# motor1 = left motor, motor2 = rightmotor
# uses WaveshareHat
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

def boolMoveThread(dt, s1, s2, mbool=None):
	if mbool != None : 
		kit.motor1.throttle = s1
		kit.motor2.throttle = s2
		time.sleep(dt - h) # little const to be taken into account because of multithreading
	else : 
		# means a condition is passed as argument, may not be useful
		while mbool : 
			kit.motor1.throttle = s1
			kit.motor2.throttle = s2

#--------------  MAIN FUNCS  -----------------

def rotate(dtheta, ws=0.1)
	# fonction basique pour tourner d'un angle dtheta, avec une vitesse lente sur chaque roue (ws)
	# dtheta en radians, ws dans [0, 1]
	dx = dtheta * width
	dt = abs(dx / ws)
	th = boolMoveThread(dt, s1=ws, s2=-ws)
	th.start()


def forward(dx): 
	# fonction basique permettant d'aller de dx vers l'avant
	dt = dx / speed
	th = threading.Thread(target=boolMoveThread, s1=speed, s2=speed)
	th.start()

	
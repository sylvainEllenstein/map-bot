#!/usr/bin/python3

# File that manages connection with robot using bluedot and gpiozero, and allows to control manually the movement 
# This is only an API for facilitating communication with servos and motors

from gpiozero import *
from signal import pause
from time import *
import threading
from adafruit_servokit import * # only using ServoKit ?

# Other custom localisation scripts are to be imported ...

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

class boolMoveThread(threading.Thread) :
	# This type of thread is to be created within a forward or backward function, and it lets run the main motors until a condition
	# becomes False (called by boolFunc); may be used within another type of function :
	def __init__(self, boolFunc, speed) :
		threading.Thread.__init__(self)
		self.boolFunc = boolFunc
		self.speed = speed
		
	def run(self) :
		kit.continuous_servo[1].throttle = self.speed
		kit.continuous_servo[2].throttle = - self.speed
		while boolFunc():
			pass
		kit.continuous_servo[1].throttle = kit.continuous_servo[2]

def forward(boolFunc, speed=1):
	# starting here a new thread would be nice...
	# then call a function that close both servos
	thread1 = boolMoveThread(boolFunc, speed)
	thread1.start()
	
	
	

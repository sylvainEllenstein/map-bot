# Python script to get localisation in space around

########### SENSORS INPUTS MANAGEMENT ############

# public data : estimatePosition() : returns an estimation of the state when called
# estimateSpeed()
# estimateRotation() (of head)

from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from mpu6050 import mpu6050
from global_funcs import *

# HC-SR04, distance sensor

myFactory = PiGPIOFactory()
distanceSensor = DistanceSensor(max_range=4, pin_factory=myFactory, echo=..., trig=...)

# accel_sensor mpu6050
accelSensor = mpu6050(0x68)

def getAccelerationData() : 
    return accelSensor.get_accel_data()

def getGyroData() : 
    return accelSensor.get_gyro_data()


############  GETTING LOCALISATION  ##############

# possible libs : filterpy, pykalman
# https://filterpy.readthedocs.io/en/latest/kalman/KalmanFilter.html

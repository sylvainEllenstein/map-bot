# Python script to get localisation in space around + get points around


#  SENSORS INPUTS MANAGEMENT #


from mpu6050 import mpu6050
from global_funcs import *
import numpy as np
import time


# accel_sensor mpu6050
accelSensor = mpu6050(0x68)  # ATTENTION : réglé en i2c, mettre un port virtuel


def get_acceleration_data() :
    return np.array(accelSensor.get_accel_data())


def get_gyro_data() :
    return np.array(accelSensor.get_gyro_data())


#  INTEGRATERS  #


def integrate_acceleration(previous_speed_vec: np.array, previous_position_vec: np.array, dt: np.float):
    accel_vec = get_acceleration_data()
    speed = np.array(accel_vec * dt + previous_speed_vec)
    position = np.array(speed * dt + previous_position_vec)
    
    # ajouter un sleep convenable, car lancé dans un thread externe ou subproc
    time.sleep(dt - h)
    return speed, position


def integrate_angle(previous_angle: np.float, dt: np.float):
    gyro_speed = get_gyro_data()
    angle = np.array(gyro_speed * dt + previous_angle)
    return angle


def speed_from_motors():
    ...


def integration_thread():
    ...  # doit être plutôt créé dans le main ?

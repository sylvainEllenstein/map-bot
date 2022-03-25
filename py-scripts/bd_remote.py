from bluedot import BlueDot
import time as tm
# from signal import pause
import numpy as np
from adafruit_motorkit import Motorkit
from moves import rectMove, rotation, getDistance

kit = MotorKit(0x40)
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

default_speed = 1
slow_speed = 0.5
left_turning, right_turning = False, False


def left_forward(speed=default_speed):
    kit.motor1.throttle = speed


def right_forward(speed = default_speed):
    kit.motor2.throttle = speed


def right_back(speed=slow_speed):
    right_forward(-speed)


def left_back(speed=slow_speed):
    left_forward(-speed)


def stop_right():
    kit.motor2.throttle = 0


def stop_left():
    kit.motor1.throttle = 0


def stop():
    stop_left()
    stop_right()


def test1():
    """"
    def begin_remote():
        bd = BlueDot(cols=3, rows=2)

        bd[1, 0].visible = False
        bd[1, 1].visible = False

        bd[0, 0].when_pressed = left_forward
        bd[0, 1].when_pressed = left_back
        bd[2, 0].when_pressed = right_forward
        bd[2, 1].when_pressed = right_back

        bd[0, 0].when_released = bd[0, 1].when_released = stop_left
        bd[2, 0].when_released = bd[2, 1].when_released = stop_right

    X = np.array([0, 0])
    actual_speed = 0
    """
    # test 1, suite de déplacements en autonomie
    # test 2 : calculer dx, diviser par 3 pour avoir en ?.s-1
    # OK pour le moment en autonomie prévue, sans utiliser bluedot et numpy
    left_forward()
    right_forward()
    # scanner la distance ici
    tm.sleep(3)
    # rescanner ici
    stop()

    left_back(0.2)
    tm.sleep(1.5)
    left_forward(0.2)
    stop_left()

    tm.sleep(1)

    left_forward(0.3)
    right_back(0.3)
    tm.sleep(2)
    stop()

    tm.sleep(1)

    left_back(0.5)
    right_back(0.5)
    tm.sleep(2.5)
    stop()

    tm.sleep(1)

    left_forward(1)
    right_forward(1)
    tm.sleep(4)
    stop()

    tm.sleep(1)

    left_back(0.6)
    right_forward(0.6)
    tm.sleep(3)
    stop()

    print("Done !")


def test2():






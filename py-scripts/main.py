# Hello there

from moves import *
from map_drawing import *
from localisation import *
import threading
import time
import gpiozero

def theBigMain():
    t0 = time.monotonic()
    theta = 0
    X, Y = 0, 0
    first_instructions = sayHello()


# And ...

if __name__ == "main" : 
    theBigMain()
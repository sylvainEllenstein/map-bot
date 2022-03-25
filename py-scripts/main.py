# Hello there
import numpy as np

from moves import *
from global_funcs import index_min
# from localisation import *
# from map_drawing import *


def detect_keys():
    """
    :return: int
    Permet d'écouter une entrée standard pour recevoir des instructions en temps réel
    """
    ...

# #############  MODES FUNCTIONS  #############


"""
 faire un brouillon un système de sycnhronisation des fonctions dans le main()
 chaque fonction doit occuper le thread principal jussqu'à la fin de son action
 les fonctions retournent dans le main() un signal qui indique l'état : (dresser une liste)
 Notes sur threads : 
    - attention aux RuntimeError en lançant deux fois le même Thread (classe à créer, pour cloner) 
    - pour kill : global flag ?  
"""

# ##################  MAIN  ###################


def main():
    t0 = time.monotonic()

    # first_instructions = say_hello()  # --> commence à diverger ici
    # mode = "working" or "scanning" or "moving"
    mode = "scanning"
    # STRUCTURE 0 : ne retient rien du tout, se déplace juste aléatoirement
    mainloop0 = lambda: 1

    def scan0(angle: np.float):
        """
        :return: float, float # angle, distance
        """
        points = get_points_map()
        i = index_min(points)
        best_angle = -45 + (angle_unit * i)
        return best_angle + angle, points[i] - 35

    def move0(new_angle, distance):
        r = RectMove(np.array([distance * cos(new_angle), distance * sin(new_angle)]))
        return MovesStack([Rotation(new_angle), r])

    mainloop = mainloop0
    new_angle, distance = scan0(angle)
    stack = move0(new_angle, distance)
    mode = "moving"
    while mainloop():
        if mode == "scanning":
            new_angle, distance = scan0(angle)
            stack = move0(new_angle, distance)
            mode = "moving"
        elif mode == "moving":
            stack.exec_stack()
            mode = "scanning"
        else:
            print("WARNING : Mode Error in main.py, main() --> invalid mode")


if __name__ == "main":
    try:
        main()
    finally:
        cleanup()

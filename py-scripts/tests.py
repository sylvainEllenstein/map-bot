#!usr/bin/python3

"""
Liste des fonctions à tester indépendamment :

0. bonne importation des scripts

MovesStack
smooth forwards
*** get_point_map
*** somme des angles (bien orienté lorsque la tête tourne, etc ...
moteurs 1 et 2 à ne pas inverser

"""
from moves import *
import time


def test_get_points():
    """
    test : not passed yet
    :return:
    """
    points = get_points_map()
    with open("/home/pi/projet/pmaps", "x") as file:
        for i in points:
            file.write(f"{i}")


def test_stack1():
    """
    test : not passed yet
    :return:
    """
    mstack1 = MovesStack([
        Rotation(3.141592),
        RectMove(),
        Rotation(3.141592 / 2),
        RectMove(60),
        Rotation(4 * 3.141592/9),
        RectMove(90)
    ])
    mstack1.exec_stack()


def test_lidar_time(t0=0.05, step=0.05, n_tries=20):
    """
    test : PASSED ON 12/03/2022
    :param t0:
    :param step:
    :param n_tries:
    :return:
    """
    l = get_distance_lidar()
    for i in range(n_tries):
        time.sleep(t0 + step * i)
        l = get_distance_lidar()
        if l is not None:
            print(f"OK with i = {i}, total = {t0 + step * i}")
        else :
            print(f"did not work with i = {i}")
        return i


def test_smooth_head_angles():
    """
    test : PASSED ON 12/03/2022
    :return:
    """
    set_smooth_angle(-30)
    print("angle = -30")
    time.sleep(1)
    set_smooth_angle(30)
    print("angle = 30")
    time.sleep(1)
    set_smooth_angle(45)
    print("angle = 45")
    time.sleep(1)
    set_smooth_angle(-45)
    print("angle = -45")
    time.sleep(1)
    set_smooth_angle(0)
    print("Back to zero!")

# Script that will contain the necessary global consts and funcs, and the conventions associated with them
# Angle convention : space is oriented counterclockwise

from math import sqrt, acos, pi
import numpy as np

bot_length = 10.5
bot_width = 4.5  # corresponds to radius, or width/2
dt = 0.08  # for the moment --> min 12 Hz
h = 0.0001  # takes a little epsilon for sleeps
little_theta = 0.04  # angle négligeable
little_norm = 0.5  # longueur négligeable

# CONVENTION DES TYPES :
"""
np.float : size de 24
np.array de np.float
"""


def sample(func, duration, freq=0.05):
	n = int(duration / freq)
	for i in range(n):
		print(f"f(t) = {func(i * freq)}")


def rotation_angle(vec1: np.array, vec2: np.array):
	# angles des vecteurs à +- pi : optimiser à 2pi près pour avoir les plus petit en valeur aboslue
	assert vec1.size == vec2.size, "Error while using rotationAngle() in global_funcs"
	if np.dot(vec1, vec2) > 0:
		return acos(norm(vec1) * norm(vec2) / np.dot(vec1, vec2))
	elif np.dot(vec1, vec2) < 0:
		return acos(norm(vec1) * norm(vec2) / np.dot(vec1, vec2)) + pi
	return pi/2


def optimized_angle(angle: np.float):
	angle %= 2 * pi
	if abs(angle - 2 * pi) < angle:
		return angle - 2 * pi
	return angle


def radians(degrees):
	return pi * degrees/180


def norm(vector):
	return sqrt(sum(i**2 for i in vector))


def say_hello():
	# function of initialisation, may get instructions to do
	print("Welcome in the bot program execution. Display of this message means all scripts were compiled without errors.")
	inp = input("First instructions : ")
	return inp


def index_min(liste: list):
	m = 0
	for i in range(len(list) - 1):
		if liste[i] <= liste[m]:
			m = i
	return m


def sign(x):
	try:
		return x / abs(x)
	except ZeroDivisionError:
		return 0

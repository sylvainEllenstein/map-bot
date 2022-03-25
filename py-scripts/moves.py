#!/usr/bin/python3

# File that manages connection with robot using bluedot and gpiozero, and allows to control manually the movement
# API pour faciliter la communication avec les moteurs, servos et capteurs

import numpy as np
import time
import threading
from global_funcs import norm, little_norm, little_theta, bot_width, bot_length, rotation_angle, optimized_angle, sign
import gpiozero
from math import *
from adafruit_motorkit import MotorKit
import pigpio
import os

# ------------------ CONSTANTS  ------------------------
os.system('export GPIOZERO_PIN_FACTORY=pigpio')

h = 0.0001
std_speed = 0.8  # pas encore 1, pour essais seulement
little_sleep_time = 0.1
angle_unit_deg = 2
angle_unit_rad = radians(angle_unit_deg)  # correspond à ~3° en rad, sert pour le scan de la zone
x, angle = np.zeros(2), 0
d_x = np.zeros(2)
lidar_latency_time = 0.08
motor_speed_epsilon = 0.05
max_speed = 1 - motor_speed_epsilon
throttle_unit = 15  # distance en cm parourure par une roue lors d'un déplacement pendant 1 sec à throttle = 1.0
# transformer en fonction, régression ?
cst_speed_for_rotation = 0.2  # vitesse de rotation par défaut
cst_speed_little_move = 0.25  # vitesse pour mouvements rect < 8 cm
# ------------------  PHYSICAL PINS ATTRIBUTION ----------------

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
try:
	distanceSensor = gpiozero.DistanceSensor(max_distance=1, echo="GPIO18", trigger="GPIO17")
except OSError:
	print("Error while trying importing pigpio, activating pigpiod")
	os.system('sudo pigpiod')
	distanceSensor = gpiozero.DistanceSensor(max_distance=1, echo="GPIO18", trigger="GPIO17")

headServo = gpiozero.AngularServo("GPIO14", min_angle=-90, max_angle=90)
headServo.angle = 0
blackButton = gpiozero.Button("GPIO21", bounce_time=None, hold_time=1, hold_repeat=False)


def speed_corrector(speed_func):
	"""
	Décorateur pour une fonction qui retroune deux vitesses (droite et gauche), et corrige
	:param speed_func: la fonction à corriger
	:return: fonction
	"""
	def corrected(*args, **kwargs):
		speed_left, speed_right = speed_func(*args, **kwargs)
		return max_speed * speed_left, max_speed * speed_right + motor_speed_epsilon * sign(speed_right)
	return corrected


def button_pressed():
	print("Buttton was pressed!")


blackButton.when_pressed = button_pressed


def get_distance_hc():
	return distanceSensor.distance * 100


RX = 23
pi = pigpio.pi()
pi.set_mode(RX, pigpio.INPUT)
pi.bb_serial_read_open(RX, 115200)


def get_tfmini_data():
	(count, recv) = pi.bb_serial_read(RX)
	if count > 8:
		for i in range(0, count - 9):
			if recv[i] == 89 and recv[i + 1] == 89:  # 0x59 is 89
				checksum = 0
				for j in range(0, 8):
					checksum += recv[i + j]
				checksum %= 256
				if checksum == recv[i + 8]:
					distance = recv[i + 2] + recv[i + 3] * 256
					strength = recv[i + 4] + recv[i + 5] * 256
					if distance <= 1200 and strength < 2000:
						return distance, strength
					# else:
					# raise ValueError('distance error: %d' % distance)
				# i = i + 9


def get_distance_lidar():
	try:
		return get_tfmini_data()[0] - 3.8
	except TypeError:
		print("get_distance_lidar failed once, not trying again, returning None")
		return None


def compute_distance():
	"""
	:return: np.float

	Fonction qui calcule la distance relevée à partir des capteurs de distance, en corrigeant au maximum les
	imperfections
	"""
	lidar_d = get_distance_lidar()
	hc_d = get_distance_hc()
	if not lidar_d:  # error has occured while scanning distance with Lidar
		return None  # recommencer ? attention si une recursion
	elif lidar_d < 35:  # ne pas oublier de tous convertir en cm !!!
		return (get_distance_hc() + hc_d)/2
	elif hc_d >= 99:
		lidar_d2 = get_distance_lidar()
		return (lidar_d2 + lidar_d) / 2
	else:
		return (hc_d + lidar_d) / 2


def set_head_angle(theta: np.float):
	headServo.angle = 2 * theta


def real_angle():
	return headServo.angle / 2


def smooth_head_angle(dtheta: np.float, delta_t=0.06, dangle=1.8):
	"""
	décale en douceur l'angle de la tête de dtheta, fonctionne avec une erreur de ~ 5%
	:param dtheta:
	:param delta_t:
	:param dangle:
	:return:
	"""
	n = int(dtheta / dangle)
	dangle *= sign(n)
	for i in range(abs(n)):
		print(f"i = {i}, head_angle = {headServo.angle}, adding {dangle}")
		set_head_angle(real_angle() + dangle)
		time.sleep(delta_t)


def set_smooth_angle(head_angle: np.float, delta_t=0.06, dangle=1.8):
	smooth_head_angle(dtheta=head_angle - real_angle(), delta_t=delta_t, dangle=dangle)


def get_points_map(dtp=0.22):
	"""
	Fonction qui scanne tous les deux degrés (angle_unit_deg) la distance, et retourne une liste de points obtenus

	:return:
	"""
	set_smooth_angle(-45)
	points = []
	for i in range(int(90 / angle_unit_deg) - 1):  # 1 enlevé par sécurité, regarder sinon quelle erreur d'angle
		scanned_distance = get_distance_lidar()  # fiablilité, plusieurs scans ?
		if scanned_distance is None:
			print("scanning distance failed, trying again in a moment")
			time.sleep(dtp)
			scanned_distance = get_distance_lidar()
		"""scanned_distance2 = get_distance_lidar()  # fiablilité, plusieurs scans ?
		time.sleep(0.1)
		if scanned_distance2 is None:
			print("scanning distance failed, trying again in a moment")
			time.sleep(dtp)
			scanned_distance2 = get_distance_lidar()
		scanned_distance = (scanned_distance + scanned_distance2) / 2
		"""
		head_angle = radians(headServo.angle)
		points.append(x + np.array([scanned_distance * cos(head_angle), scanned_distance * sin(head_angle)], dtype=np.float))
		time.sleep(lidar_latency_time + dtp - 0.1)
		headServo.angle += 2 * angle_unit_deg
	set_smooth_angle(0)
	return points


# ------------------  MAIN FUNCS AND CLASSES  ---------------------


def activate_motors(speed, dt, sample_frequency=0.05, keep_moving=None):
	"""
	Fait tourner les moteurs gauche à vitesse speed pendant dt secondes (puis les stoppe)
	---> à améliorer en ajoutant une condition éventuelle de blocage au milieu
	Pour être lancée dans un thread parallèle
	:param speed: fonction qui retourne deux float dans [-1, 1], pour la vitesse des moteurs gauche et droit
	:param dt: float > 0, durée du déplacement
	:param sample_frequency: période d'échantillonage de la fonction speed
	:param keep_moving: fonction sans arguments qui permet de couper au milieu le mouvement

	:return: None
	"""
	n = int(dt / sample_frequency)
	if keep_moving is None:
		keep_moving = lambda: True
	for i in range(n):
		if not keep_moving():
			break
		kit.motor1.throttle, kit.motor2.throttle = speed(i * sample_frequency)  # moteur droit en retard ? moins rapide
		time.sleep(sample_frequency)
	kit.motor1.throttle = kit.motor2.throttle = 0.0


# Ici, les routines pour les fonctions de vitesse lors des déplacements


def calibrate_cst_speed(speed, dt, freq=0.2):
	"""
	Fonction pour visualiser une vitesse constante pendant un certain temps et faire la conversion en cm
	:param speed: float dans [-1, 1] la vitesse visualisée
	:param dt: temps de parcours en secondes
	:param freq: fréquence de relevé de la distance avec HC-SR04
	:return: liste ? moyenne ? print direct --> None ?
	"""
	d0 = (get_distance_hc() + get_distance_hc()) / 2
	distances = [d0]
	n = int(dt / freq)
	print(f'd0 = {d0} cm')
	time.sleep(1)

	def speed_func(t):
		if t <= dt:
			return speed, speed

	th = threading.Thread(target=activate_motors, args=(speed_func, dt))
	th.start()
	for i in range(n):
		d = get_distance_hc()
		print(f'd = {d} cm')
		distances.append(d)
		time.sleep(freq - h)
	deltas = [distances[i + 1] - distances[i] for i in range(len(distances) - 1)]
	average_delta = sum(deltas) / len(deltas)
	print(f'average_delta = {average_delta} cm')
	average_speed = average_delta / freq
	print(f'average speed = {average_speed} cm.s-1')


def accel_phase(final_speed=1, duration=1):
	"""
	Gère la phase d'accélération en douceur selon la vitesse à atteindre et le temps total
	pour améliorer les résultats, étalonner ensuite
	:param final_speed: float dans [-1, 1], vitesse à atteindre à t = duration
	:param duration: float > 0, la durée du mouvement d'accélération
	:return: fonction qui donne la vitesse (float dans [-1, 1])
	"""
	coeff = sign(final_speed) * 0.88 * final_speed / duration
	v0 = 0.12 * sign(final_speed)

	def accel(t):
		return v0 + coeff * t, v0 + coeff * t
	return accel


def deccel_phase(initial_speed=1, duration=1):
	"""
	Idem pour décélération
	:param initial_speed:
	:param duration:
	:return:
	"""
	accel = accel_phase(final_speed=initial_speed, duration=duration)

	def deccel(t):
		return accel(duration - t)

	return deccel


def forward_speed(length):
	"""
	Retourne la fonction de la vitesse en fonction du temps pour un déplacement rectiligne de length cm
	:param length: longueur du déplacement
	:return: fonction qui donne la vitesse
	"""
	if abs(length) <= 8:
		cst_speed_time = throttle_unit / (abs(length) * cst_speed_little_move)

		@speed_corrector
		def speed(t):
			if t <= cst_speed_time:
				return sign(length) * cst_speed_little_move, sign(length) * cst_speed_little_move
			return 0.0, 0.0

		return speed

	cst_speed_length = abs(length) - 8
	cst_speed_time = max_speed * cst_speed_length / throttle_unit
	accel = accel_phase(final_speed=1)
	deccel = deccel_phase(initial_speed=1)

	@speed_corrector
	def speed(t):
		if t <= 1:  # le 1 est lié à la durée de l'accélération, à regarder avec accel_phase !
			return [sign(length) * i for i in accel(t)]
		if t <= 1 + cst_speed_time:
			return sign(length), sign(length)
		if t <= cst_speed_time + 2:
			return [sign(length) * i for i in deccel(t - cst_speed_time - 1)]
		return 0.0, 0.0

	return speed


def rotate_speed(theta):
	"""
	Idem pour une rotation d'angle theta
	:param theta: en radians, l'angle de la rotation à effectuer (optimisé de préférence, cf global_funcs)
	:return: Fonction qui donne la vitesse en fonction de t (> 0)
	"""
	perimeter = theta * bot_width / 2
	cst_speed_time = abs(perimeter) / (cst_speed_for_rotation * throttle_unit)

	@speed_corrector
	def speed(t):
		if t <= cst_speed_time:
			return sign(theta) * cst_speed_for_rotation, - sign(theta) * cst_speed_for_rotation
		return 0.0, 0.0

	return speed


def rotate(theta, joining=False):
	"""
	Fonction qui lance concrètement un thread de rotation d'angle theta
	:param theta: angle en radians
	:param joining: si le thread parallèle est attendu au bout
	:return:
	"""
	duration = abs(theta) * bot_width / (2 * cst_speed_for_rotation * throttle_unit)

	th = threading.Thread(target=activate_motors, args=(rotate_speed(theta), duration))
	th.start()
	if joining:
		th.join()


def forward(length, joining=False):
	# fonction basique permettant d'aller de dx vers l'avant --------> VERSION SMOOTH ENSUITE
	if abs(length) < 8:
		duration = length / (throttle_unit * cst_speed_little_move)
	else:
		duration = 2 + max_speed * (length - 8) / throttle_unit

	th = threading.Thread(target=activate_motors, args=(forward_speed(length), duration))
	th.start()
	if joining:
		th.join()


class RectMove:
	def __init__(self, vector: np.array, start_point=None, start_angle=None):
		self.vector = vector
		self.startAngle = start_angle
		self.startPoint = start_point

	def exec(self, x: np.array, angle: np.float, joining=False):
		# méthode lancée depuis une pile de déplacements : d'abord corrige les erreurs avec approximation(),
		# puis lance un déplacement de A à B
		# but : ne pas être trop simple, intégrer le futur système de correction et détection d'obstacles
		if not (x is None and angle is None):
			self.approximation(x, angle)
		forward(norm(self.vector), joining)

	def __repr__(self):
		return f"Rect move from {self.startPoint} and angle {self.startAngle} with vector norm {self.vector}"

	def next_position(self):
		delta_x = self.vector
		return delta_x, 0

	def approximation(self, x: np.array, angle: np.float):
		"""
		Méthode pour retourner l'erreur entre les conditions de départ du mouvement et les conditions actuelles
		--> utile ? corrige l'approximation ou retourne
		:param x:
		:param angle:
		:return:
		"""
		...


class Rotation:
	def __init__(self, angle: np.float, start_point=None, initial_angle=None):
		self.startAngle = initial_angle
		self.angle = angle
		self.startPoint = start_point

	# cette classe reprend les mêmes méthodes que la classe précédente

	def __repr__(self):
		return f'Rotation from {self.startPoint} of angle {self.angle}'

	def exec(self, x, angle, joining=False):
		if not (x is None and angle is None):
			self.approximation(x, angle)
		rotate(self.angle, joining=joining)

	def next_position(self):
		return np.zeros(2), self.angle

	def approximation(self, x, angle):
		# same that for rectMove()
		if self.startPoint is not None:
			delta_vec = x - self.startPoint
			delta_theta = angle - self.startAngle
			if delta_theta > little_theta:
				...
			if norm(delta_vec) > little_norm:
				...


class MovesStack:
	# regarder si déjà des libes python pour optimiser des stacks / files
	def __init__(self, moves: list):
		self.stack = moves

	def exec_stack(self, joining=False):
		"""
		Méthode de moves stack pour lancer une
		:param joining:
		:return:
		"""
		global x
		global angle
		for mv in self.stack:
			d_x, d_angle = mv.next_position()
			mv.exec(x, angle, joining)
			x += d_x
			angle += d_angle

	def append(self, *args, **kwargs):
		self.stack.append(*args, **kwargs)

	def __repr__(self):
		return str(mv.__repr__() + "\n" for mv in self.stack)

	def simulation(self, plt_mode: str, ang0=1.57079632):
		print("Displaying a visual interface for the moves stack")
		if plt_mode in ("vectors", "norms"):
			try:
				import matplotlib.pyplot as plt
			except ImportError:
				print("No visual interface could be loaded, writing movesStack in a file")
				plt_mode = "file"
		ang = ang0
		x, y = [0], [0]
		pos = np.array([0.0, 0.0])

		if plt_mode == "vectors":
			for mv in self.stack:
				if type(mv) == RectMove:
					pos += mv.vector
					x.append(pos[0])
					y.append(pos[1])
			plt.plot(x, y)
			plt.show()

		elif plt_mode == "norms":
			for mv in self.stack:
				if type(mv) == Rotation:
					ang -= mv.angle  # to match trigonometric sense
				else:
					vec_norm = norm(mv.vector)
					pos += np.array([cos(ang) * vec_norm, sin(ang) * bot_length])
					x.append(pos[0])
					y.append(pos[1])
			plt.plot(x, y)
			plt.show()

		elif plt_mode == "file":
			from datetime import datetime
			dtstring = datetime.now().strftime("%d/%m/%Y%  %H:%M:%S")
			try:
				moves_data = open("moves_stack_data.txt", "w")
			except FileNotFoundError:
				moves_data = open("moves_stack_data.txt", "x")
			moves_data.write(dtstring + "\n")
			moves_data.write(f"length = {len(self.stack)}" + "\n")
			for mv in self.stack:
				if type(mv) == Rotation:
					moves_data.write(f"rotation : {mv.angle}" + "\n")
				else:
					moves_data.write(f"rectmove : {mv.vector}" + "\n")
			moves_data.write("\n")
			moves_data.close()

# ------------------  OTHER FUNCTIONS USING CLASSES ------------------- #


def vectors_to_stack(vectors: list, X: np.array, angle: np.float):
	"""
	:param vectors: list(np.array)
	:return: MovesStack

	Takes as argument a list of vectors, and return a MovesStack instance that executes the movement
	ne pas oublier de régler les problemes d'initialisation, dès le début (angle de départ à corriger)
	"""
	# fonctions requises : calcul d'angles et de normes de vecteurs
	mstack = MovesStack([])
	for vec in vectors[1:]:
		angle = rotation_angle(mstack.stack[-1], vec)
		if angle > little_theta:
			mstack.append(Rotation(angle=optimized_angle(angle)))
		mstack.append(vec)

	return mstack


def points_to_vector(points: list):
	start_point = points[0]
	vectors = [points[i + 1] - points[i] for i in range(len(points) - 1)]

	return start_point, vectors

# fonctions globales restantes à coder : detect_holes, class graph avec méthode add_points (quel algo pour un graphe
# le plus efficace possible ? regarder aux alentours avant de couper plusieurs arêtes
# fonction smooth_forward() etc ...


def cleanup():
	print('Cleaning everything up, restart moves.py if needed')
	headServo.angle = 0
	kit.motor1.throttle = 0.0
	kit.motor2.throttle = 0.0

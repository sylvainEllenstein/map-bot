# py file intended to draw a map with informations collected from localisation.py
"""
creates instructions lists : at this step, the only informations are the points collected in localisation

draws maps with instructions files : this command writes in a SVG file, and takes as argument a precision
indicator (how it relies the points together) and an angle precision indicator (how it relies 3 points on
a same direction)

This script has to manage two important things : the informations from sensors and the estimation of the position
Plus, this position must be usable for some other scripts, and particularly the one building the map (and the 
informations from sensors too ?)

Global classes / functioning

a process to manage the kalman filtering : this can access to the previous position and the informations of the sensors
but not much more...
a map class / or file ? that can be exported to graphical representation or for other scrripts that need it (when back
on an already mapped space, it would be useful to have an algorithm to recognise the position... and so to be able to 
go from an A to a B point)

--------------------

DRAWING ALGORITHM 0: points simples
- reads each line of the file, calculates the distance between the points, determines if they are (or may be ?) connected
  - if yes : adds a line to draw between the 2 points
  - if no : adds to drawlist only a point

--------------------

DRAWING ALGORITHM 1:  rectiligne
- ensemble de droites --> segments plutôt...
--> pour chaque point on détermine si il appartient ou non à une des droites ou on en créé une autre (?)

Then final step : reads the draw instructions file
- returns a svg file
- converts to PNG for portability, OR : transfers SVG file to user interface for annotation
-> then converts to PNG (not mandatory)
"""
import numpy as np
from moves import get_points_map, angle_unit


class MapFile:
    def __init__(self, filename: str):
        self.file_location = f"./rene-main/draw_files/{filename}"
        try:
            x = open(self.file_location, 'x')
            x.close()
            del x
        except FileExistsError:
            print("FILE CREATION ERROR : MapFile instance could not be created (FileExistsError")

    def add_points(self, points: list, X: np.array, angle: np.float):
        """
        :param points:
        :param X:
        :param angle:
        :return: NoneType

        Ecrit dans un fichier les points relevés, et les ajoute à un fichier de points, en les replaçant correctement
        """
        points = get_points_map()

        with open(self.file_location, "w") as file:
            file.writelines(points)

    def convert_to_svg(self):
        ...


"""
AUTRE PB :
Comment créer le graphe discret pour effectuer les algos ?
fonction detect_holes à créer ... à quel endroi dans le code
regarder comment caractériser un espace fermé, et réfléchir à quand le détecter ...

"""


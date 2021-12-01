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

Creation of a drawlist file to give to drawing 
- reads each line of the file, calculates the distance between the points, determines if they are (or may be ?) connected
  - if yes : adds a line to draw between the 2 points
  - if no : adds to drawlist only a point 
  
Then final step : reads the draw instructions file
- returns a svg file
- converts to PNG for portability, OR : transfers SVG file to user interface for annotation
-> then converts to PNG (not mandatory)
"""
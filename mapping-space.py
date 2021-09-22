# Python script to map scpace around
"""
Algorithm explanation :

- Rotate the distance sensor
- scan at every moment the distance
  --> states the position in relation to the tags
  --> states the distance
  -> stores informations in a file (or in a matrix)
- ... repeats this sequence during one sensor rotation

Compiling :
- problematics : how to represent the points in a 2D map ?
- how to limit space scanning (stops processing, and draw map) : rect. dimensions ? timeout ? 

Creation of a drawlist file to give to drawing 
- reads each line of the file, calculates the distance between the points, determines if they are (or can ?) connected
  - if yes : adds a line to draw between the 2 points
  - if no : adds to drawlist only a point 
  
Then final step : reads the draw instructions file
- returns a svg file
- converts to PNG for portability, OR : transfers SVG file to user interface for annotation
-> then converts to PNG (not mandatory)
"""

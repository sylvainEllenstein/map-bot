# Script that manages the interactions with tags
# OR 
# manages the position alone (risk of inaccuracy...)

"""
Example of algorithm without tags : 

Once the robot chooses to move : 
- put distance sensor forward
- scan distance
- go forward while needed, and scan (moreless) continuously while the target isn't reached

problem : not precise when an infinite distance is detected
--> test actual sensor
--> change for a more precise (best range) sensor

"""

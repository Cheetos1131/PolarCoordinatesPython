import math, turtle, subprocess
from Rose import RoseCurve

screen2 = turtle.Screen()
screen2.setup(width=1080, height=1920, startx=0, starty=0)
screen2.bgcolor('black')

startDeg = 0
endDeg = 360
n = 100
d = 97

RoseCurve(startDeg, endDeg, n, d)
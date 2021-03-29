import math, turtle

screen1 = turtle.Screen()
screen1.setup(width=1080, height=1920, startx=0, starty=0)
turtle.title('Rhodonea Curve')
screen1.bgcolor('black')
rose = turtle.Turtle()
rose.speed(20)

startDeg = 0
endDeg = 360
n = 100
d = 97


def RoseCurve(startDeg, endDeg, n, d):
    rose.color('blue')
    rose.pensize(0.5)
    rose.hideturtle()
    for theta in range(startDeg, endDeg + 1, 1):
        k = theta * d * math.pi / 180 # Conversion to radian degrees
        r = 300 * math.sin(n * k) # Getting the radius
        x = r * math.cos(k) # Getting the X coordinate
        y = r * math.sin(k) # Getting the Y coordinate
        rose.goto(x, y) # Setting the point to be drawn
    rose.goto(0,0) # Reset point for the rose curve drawing

    rose.color('red')
    rose.pensize(4)
    for theta in range(startDeg, endDeg + 1, 1):
        k = theta * math.pi / 180
        r = 300 * math.sin(n * k)
        x = r * math.cos(k)
        y = r * math.sin(k)
        rose.goto(x, y)
    screen1.exitonclick()

RoseCurve(startDeg, endDeg, n, d)
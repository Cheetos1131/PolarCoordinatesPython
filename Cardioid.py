import math, turtle

screen2 = turtle.Screen()
screen2.setup(width=1080, height=1920, startx=0, starty=0)
turtle.title("Cardioid")
screen2.bgcolor('black')
cardioid = turtle.Turtle()
cardioid.pensize(4)
cardioid.color("red")

startDeg = 0
endDeg = 360
r = 75

def Cardioid(startDeg, endDeg, r):
    
    cardioid.penup()
    cardioid.goto(150, 0)
    cardioid.pendown()
    cardioid.hideturtle()

    for degrees in range(startDeg, endDeg + 1):
        rads = math.radians(degrees)
        distance = (1 + math.cos(rads)) * r
        x = math.cos(rads) * distance
        y = math.sin(rads) * distance
        cardioid.goto(x, y)   
    screen2.exitonclick()

Cardioid(startDeg, endDeg, r)
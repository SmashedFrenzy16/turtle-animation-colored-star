import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

t.speed(500)
s.bgcolor('black')

colours = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']

for star in range(490):
    t.pencolor(colours[star%6])
    t.width(star / 250 + 1)
    t.fd(star);t.left(210)

t.hideturtle()
time.sleep(10)
s.bye()

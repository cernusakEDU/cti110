# Jeremiah Cernusak
# 11/03/2024
# P4LAB1a
# Turtle Shape Drawer

import turtle

wn = turtle.Screen()
wn.bgcolor("white")

shape_turtle = turtle.Turtle()
shape_turtle.speed(1)

for i in range(4):
    shape_turtle.forward(100)
    shape_turtle.right(90)

shape_turtle.penup()
shape_turtle.goto(0, -110)
shape_turtle.pendown()

for i in range(3):
    shape_turtle.forward(100)
    shape_turtle.right(120)

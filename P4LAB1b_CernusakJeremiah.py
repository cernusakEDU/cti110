# Jeremiah Cernusak
# 11/03/2024
# P4LAB1b
# Turtle Initial Drawer

import turtle

wn = turtle.Screen()
wn.bgcolor("black")

initial_turtle = turtle.Turtle()
initial_turtle.speed(1)
initial_turtle.color("white")

# J
initial_turtle.forward(20)
initial_turtle.right(90)
initial_turtle.forward(100)
initial_turtle.right(90)
initial_turtle.forward(70)
initial_turtle.right(90)
initial_turtle.forward(20)
initial_turtle.right(90)
initial_turtle.forward(50)
initial_turtle.left(90)
initial_turtle.forward(80)

initial_turtle.penup()

initial_turtle.right(90)
initial_turtle.forward(35)

initial_turtle.pendown()

# C
initial_turtle.forward(70)
initial_turtle.right(90)
initial_turtle.forward(20)
initial_turtle.right(90)
initial_turtle.forward(50)
initial_turtle.left(90)
initial_turtle.forward(60)
initial_turtle.left(90)
initial_turtle.forward(50)
initial_turtle.right(90)
initial_turtle.forward(20)
initial_turtle.right(90)
initial_turtle.forward(70)
initial_turtle.right(90)
initial_turtle.forward(100)


turtle.done()

#-------------------------------------------------------------------------------
# Name:        turtleclock
# Purpose:     Draw a clock face with turtles on it
#
# Author:      David
#
# Created:     05/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.bgcolor("seagreen")

freshie = turtle.Turtle()
freshie.shape("turtle")
freshie.color("blue")
freshie.pensize(3)

freshie.stamp()

for a in range(12):
    freshie.penup()
    freshie.forward(90)
    freshie.pendown()
    freshie.forward(5)
    freshie.penup()
    freshie.forward(15)
    freshie.stamp()
    freshie.forward(-110)
    freshie.left(360/12)

freshie.hideturtle()

wn.mainloop()

print(type(freshie))
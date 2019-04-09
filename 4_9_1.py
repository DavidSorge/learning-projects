#-------------------------------------------------------------------------------
# Name:        Exercise 4.9.1
# Purpose:     Fruitful and Void Function practice
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_square(T,l):
    """
    Tells a turtle T to draw a square with sides of length l
    """
    for i in range(4):
        T.forward(l)
        T.left(90)

wn = turtle.Screen()        # Create Turtle Screen
wn.bgcolor("lightgreen")
wn.title("five squares")

marko = turtle.Turtle()     # Create Marko the hot pink turtle
marko.pensize(3)
marko.color("hotpink")

for j in range(5):
    marko.pendown()
    draw_square(marko,20)
    marko.penup()
    marko.forward(40)


wn.mainloop()

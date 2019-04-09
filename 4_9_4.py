#-------------------------------------------------------------------------------
# Name:        4.9.4
# Purpose:     Draw more pretty patterns
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

wn = turtle.Screen()        # Creates Turtle Screen
wn.bgcolor("lightgreen")
wn.title("pretty pattern")

marko = turtle.Turtle()     # Creates Marko the hot pink turtle
marko.pensize(3)
marko.color("blue")
marko.speed(0)

for i in range(20):
    draw_square(marko,100)
    marko.right(360/20)

wn.mainloop()

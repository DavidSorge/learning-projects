#-------------------------------------------------------------------------------
# Name:        4.9.2
# Purpose:      Draw Squares
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
wn.title("five squares")

marko = turtle.Turtle()     # Creates Marko the hot pink turtle
marko.pensize(3)
marko.color("hotpink")
marko.speed(3)

length = 20

for i in range(5):
    marko.pendown()           # Tells Marko to draw a square
    draw_square(marko,length)

    marko.penup()             # Tells Marko to move to start position for next square
    marko.backward(10)
    marko.right(90)
    marko.forward(10)
    marko.left(90)

    length = length + 20     # Tells Marko how much bigger the next square should be

wn.mainloop()
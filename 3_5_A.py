#-------------------------------------------------------------------------------
# Name:        3.5.10
# Purpose:     Drawing stars with Turtles
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_star(t, sz):
    """
    Tells turtle t to draw a star with sides of length sz.
    """
    for i in range(5):
        t.forward(sz)
        t.right(144)


wn = turtle.Screen()        # Create Turtle Screen
wn.bgcolor("lightgreen")
wn.title("five stars")

marko = turtle.Turtle()     # Create Marko the hot pink turtle
marko.pensize(3)
marko.color("hotpink")

marko.penup()
marko.backward(175)
marko.pendown()

for i in range(5):
    draw_star(marko, 100)
    # marko.penup()
    marko.forward(350)
    marko.right(144)
    # marko.pendown()


wn.mainloop()

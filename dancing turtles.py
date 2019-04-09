#-------------------------------------------------------------------------------
# Name:        Alex and Tess Dancing
# Purpose:
#
# Author:      David
#
# Created:     08/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def make_window(colr, ttle):
    """
    Set up the window with the given background color and title.
    Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    """
    Set up a turtle with the given color and pensize.
    Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

tess.forward(10)
alex.forward(-10)
dave.right(90)
dave.forward(10)
dave.left(90)

wn.mainloop()
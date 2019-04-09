#-------------------------------------------------------------------------------
# Name:        Tess meets a function
# Purpose:
#
# Author:      David
#
# Created:     05/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
__import__("turtle").__traceable__ = False

def draw_multicolor_square(t,sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()    # Sets up the window and its attributes
wn.bgcolor("seashell")

tess = turtle.Turtle()  # Create tess and set some attributes
tess.pensize(3)
tess.speed(0)

size = 20               # Size of the smallest square
for i in range(30):
    draw_multicolor_square(tess, size)
    size = size + 10
    tess.forward(10)
    tess.right(18)

wn.mainloop()
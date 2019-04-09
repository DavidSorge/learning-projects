#-------------------------------------------------------------------------------
# Name:        4.9.5
# Purpose:     draw spirals
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import turtle

def draw_square_spiral(T,l,i,s,a):
    """
    Tells a turtle T to draw a single round of a square-like spiral
    with starting length l, incrementally increasing width i, and number of segments s,  with angle a at the corners.
    """
    len = l     # Define variable len

    for j in range(s):
        T.forward(len)
        T.right(a)
        len = len + i

wn = turtle.Screen()                        # Creates Turtle Screen
wn.bgcolor("lightgreen")
wn.title("pretty pattern")

marko = turtle.Turtle()                     # Creates Marko the blue turtle
marko.pensize(1)
marko.color("blue")
marko.speed(0)

marko.penup()                               # Moves Marko to starting postion
marko.backward(150)
marko.pendown()
marko.right(90)

draw_square_spiral(marko, 2, 2, 103, 90)    # Draws a 90 degree square spiral

marko.penup()                               # Moves marko to a new starting position
marko.forward(350)
marko.right(90)
marko.forward(100)
marko.left(90)
marko.pendown()

draw_square_spiral(marko,2,2,103,89)        # Draws an 89 degree square spiral


wn.mainloop()
#-------------------------------------------------------------------------------
# Name:        4.9.3
# Purpose:      Draw Regular Polygons
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_poly(t,n,l):
    """
    Tells a turtle t to draw a regular polygon with n sides of length l
    """
    for i in range(n):
        t.forward(l)
        t.left(360/n)

wn = turtle.Screen()        # Creates Turtle Screen
wn.bgcolor("lightgreen")
wn.title("polygon")

marko = turtle.Turtle()     # Creates Marko the hot pink turtle
marko.pensize(3)
marko.color("hotpink")
marko.speed(3)

numbers = (12, 11, 10, 9 , 8 , 7 , 6 , 5 , 4 , 3)

for n in numbers:
    draw_poly(marko,n,50)
    n = n - 1

wn.mainloop()
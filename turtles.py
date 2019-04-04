#-------------------------------------------------------------------------------
# Name:        More Turtles!
# Purpose:     Watch Freshie and Freddy draw shapes!
#
# Author:      David
#
# Created:     02/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn. bgcolor("seagreen")
wn.title("Freshie and Freddy")

Freshie = turtle.Turtle()   # Create Freshie
Freshie.color('green')
Freshie.pensize(5)

Freddy = turtle.Turtle()    # Create Freddy
Freddy.color('orange red')
Freddy.pensize(3)

Freshie.forward(80)         # Draw equilateral triangle with Freshie
Freshie.left(120)
Freshie.forward(80)
Freshie.left(120)
Freshie.forward(80)
Freshie.left(120)           # Complete Triangle

Freshie.right(180)          # Turn Freshie around
Freshie.forward(80)          # Move Freshie away from origin

Freddy.forward(50)          # Draw square with Freddy
Freddy.left(90)
Freddy.forward(50)
Freddy.left(90)
Freddy.forward(50)
Freddy.left(90)
Freddy.forward(50)
Freddy.left(90)

wn.mainloop()



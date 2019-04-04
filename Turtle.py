#-------------------------------------------------------------------------------
# Name:        Freshie the Turtle
# Purpose:     Playing with the Turtle Module
#
# Author:      David
#
# Created:     02/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle               # Allows us to play with turtles
wn = turtle.Screen()        # Creates a turtle playground
wn.bgcolor('seagreen')
wn.title("Freshie and Freddie")

Freshie = turtle.Turtle()   # Create a turtle named Freshie
Freshie.color('green')
Freshie.pensize(3)



Freshie.forward(50)         # Moves Freshie forward by 50 units
Freshie.left(75)            # Turns Freshie  to the left


wn.mainloop()               # Wait for user to close window
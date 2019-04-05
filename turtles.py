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
wn. bgcolor("turquoise")
wn.title("Freshie and Freddy")

Freshie = turtle.Turtle()   # Create Freshie
Freshie.color('green')
Freshie.shape("turtle")
Freshie.pensize(5)
Freshie.speed(5)

Freddy = turtle.Turtle()    # Create Freddy
Freddy.color('orange red')
Freddy.pensize(3)
Freddy.shape("triangle")
Freshie.speed(10)

for a in range(3):
    Freshie.forward(80)         # Draw equilateral triangle with Freshie
    Freshie.left(120)

Freshie.right(180)          # Turn Freshie around
Freshie.forward(80)          # Move Freshie away from origin

#Assign a list to a variable
clrs = ["yellow", "red", "orange", "orange red"]
for c in clrs:
    Freddy.color(c)
    Freddy.forward(50)          # Draw square with Freddy
    Freddy.left(90)

Freddy.penup()
Freddy.forward(100) #moves Freddy without drawing a line
Freddy.pendown()




Stamper = turtle.Turtle()
Stamper.shape("turtle")
Stamper.color("blue")

Stamper.penup()
size = 20
for j in range(30):
    Stamper.stamp()  #Leave an impression on the canvas
    size = size + 3  #increase size with each iteration
    Stamper.forward(size)   # moves Stamper
    Stamper.right(24)       # and turns.

Stamper.color("red")

wn.mainloop()
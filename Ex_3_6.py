#-------------------------------------------------------------------------------
# Name:        Ex 3.6
# Purpose:
#
# Author:      David
#
# Created:     05/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Exercise 3.6")

tricky = turtle.Turtle()
tricky.shape("turtle")
tricky.color("red")

sequel = turtle.Turtle()
sequel.shape("turtle")
sequel.color("yellow")

hexie = turtle.Turtle()
hexie.shape("turtle")
hexie.color("green")

octa = turtle.Turtle()
octa.shape("turtle")
octa.color("blue")


tricky.penup()
tricky.forward(50)
tricky.pendown()

sequel.penup()
sequel.left(90)
sequel.forward(50)
sequel.right(90)
sequel.pendown()

hexie.penup()
hexie.forward(-50)
hexie.pendown()

octa.penup()
octa.right(90)
octa.forward(50)
octa.left(90)
octa.pendown()


for i in range(3):
    tricky.forward(20)
    tricky.left(360/3)

for i in range(4):
    sequel.forward(20)
    sequel.left(360/4)

for i in range(6):
    hexie.forward(20)
    hexie.left(360/6)

for i in range(8):
    octa.forward(20)
    octa.left(360/8)

wn.mainloop()

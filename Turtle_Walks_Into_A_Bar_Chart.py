#-------------------------------------------------------------------------------
# Name:        A Turtle walks into a bar chart
# Purpose:     Draw Bar chart with Turtle Module
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

xs = [48, 117, 200, 240, 160, 260, 220]

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height."""
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height)   # Draw up the left side
    t.right(90)
    t.write('   ' + str(height))
    t.forward(40)       # Width of the bar, along the top
    t.right(90)
    t.forward(height)   # And down again!
    t.left(90)          # Return the turtle to facing the way we found it
    t.end_fill()
    t.penup()
    t.forward(10)       # Leave a small gap after the bar

wn = turtle.Screen()        # Creates a turtle playground
wn.bgcolor('beige')
wn.title("Alex walks into a bar chart")

alex = turtle.Turtle()   # Create a turtle named Alex
alex.color('green', 'lightgreen')
alex.pensize(3)

for v in xs:
    draw_bar(alex, v)

wn.mainloop()



#-------------------------------------------------------------------------------
# Name:        Turtle Star
# Purpose:
#
# Author:      David
#
# Created:     05/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

angle = 2 * 360 / 5

wn = turtle.Screen()

penny = turtle.Turtle()

for i in range(5):
    penny.forward(50)
    penny.right(angle)

wn.mainloop()


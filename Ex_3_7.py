#-------------------------------------------------------------------------------
# Name:        module1
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
pirate = turtle.Turtle()
pirate.pensize(3)


angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

heading = 0

for a in angles:
    pirate.forward(100)
    pirate.left(a)
    heading = heading + a
    print("the pirate's current heading is", heading%360)

pirate.forward(100)

wn.mainloop()


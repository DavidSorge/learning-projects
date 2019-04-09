#-------------------------------------------------------------------------------
# Name:        Functions calling functions
# Purpose:
#
# Author:      David
#
# Created:     05/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def draw_rectangle(t,w,h):
    """Get turtle t to draw a rectangle of width w and height h"""
    for i in range(2):
        t.forwward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz) # a new version of draw_square
    """Get turtle tx to draw a square of size sz"""
    draw_rectangle(tx, sz, sz)


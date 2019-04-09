#-------------------------------------------------------------------------------
# Name:        5.9.6
# Purpose:     Sum to N
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sum_to(n):
    a = 0                       # sets a equal to zero
    for c in range(n+1):        # tells the program to repeat n+1 times (the + 1 is there because the range function returns 0 as the first number, and n-1 as the last).
        a = a + c

    return a

n = sum_to(int(input("What number forms the upper bound of your sum function?")))
print("the sum is", n)


def area_of_circle(r):
    pi = 3.141592653589
    area = pi * r ** 2
    return area

radius = input("What is the radius of your circle in meters?")
fradius = float(radius)
a = area_of_circle(fradius)
print("The area of your circle is", a, "meters squared.")

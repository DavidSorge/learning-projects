#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def find_hypot(a, b):
    """Finds the hypotenuse of a right triangle, given two sides"""
    c = (a**2 + b**2)**0.5
    return c

def approx_equal(x,y):
    """tells you that two numbers are approximately equal if the are equivalent to 5 dp"""
    if abs(x-y) < 0.00001:
        return True
    else:
        return False

def is_rightangled(i,j,k):
    l = find_hypot(i,j)         #calculate what you should expect the hypotenuse to be if k is the longest side
    m = find_hypot(j,k)         #calculate what you should expect the hypotenuse to be if i is the longest side
    n = find_hypot(i,k)         #calculate what you should expect the hypotenuse to be if j is the longest side
    if approx_equal(k,l) or approx_equal(i,m) or approx_equal(j,n): #compare expected and provided hypotenuses
        return True
    else:
        return False

def impossible_triangle(d,e,f):
    if d >= e + f or e >= d + f or f >= e + d:
        return True
    else:
        return False



side1 = float(input("How long is the first side of your triangle?"))
side2 = float(input("How long is the second side of your triangle?"))
side3 = float(input("How long is the last side of your triangle?"))

if impossible_triangle(side1,side2,side3)==True:
    print ("That's not a triangle! (At least not on a flat plane...)")
elif is_rightangled(side1,side2,side3) == True:
    print ("Congratulations! It's a right triangle!")
else:
    print ("Congratulations! You found a triangle that has no 90 degree angles!")



# hypo = find_hypot(side1,side2)

# print("The hypotenuse of your right triangle has length", hypo)

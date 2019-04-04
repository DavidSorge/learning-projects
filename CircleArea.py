#-------------------------------------------------------------------------------
# Name:        circlearea
# Purpose:     find the radius of a circle with user-given radius
#
# Author:      David
#
# Created:     02/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

response = input("What is the radius of your circle? ")
r = float(response)
area = 3.141592653589 * r ** 2
print("The area of your circle is ", area)


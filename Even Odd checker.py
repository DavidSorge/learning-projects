#-------------------------------------------------------------------------------
# Name:        even odd checker
# Purpose:     Check whether a user-input number is even or odd.
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


x = int(input("What number shall I check?"))

if x % 2 == 0:
    print(x, " is even.")
    print ("Did you know that 2 is the only even number that is prime?")
else:
    print (x, " is odd.")
    print("Did you know that multiplying two odd numbers "+"always gives an odd result?")
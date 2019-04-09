#-------------------------------------------------------------------------------
# Name:        5.14.1
# Purpose:     Days of the Week converter
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def int_to_day(n):
    if n == 0:
        return ("Sunday. He is Risen!")
    elif n == 1:
        return ("Monday, fun-day!")
    elif n == 2:
        return ("Tuesday treat!")
    elif n == 3:
        return ("Wednesday, hump day.")
    elif n == 4:
        return ("Throwback Thursday")
    elif n == 5:
        return ("Friday, thank God!")
    else:
        return ("Social Saturday")

day = int(input("What day of the week is it, numerically?"))

print(int_to_day(day))



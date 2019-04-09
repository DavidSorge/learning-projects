#-------------------------------------------------------------------------------
# Name:        5.14.1
# Purpose:     What day do I get home from vacation?
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
        return ("throwback Thursday")
    elif n == 5:
        return ("Friday, thank God!")
    else:
        return ("social Saturday")

day = int(input("What day of the week will you leave?"))
nights_slept = int(input("How many nights will you sleep (or not--you're on vacation after all!) on your vacation?"))

day = day + nights_slept

return_day = int_to_day(day)

print("You will return home on", return_day)

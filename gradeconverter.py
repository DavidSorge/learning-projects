#-------------------------------------------------------------------------------
# Name:        gradeconverter
# Purpose:     Converts logical, numerical grades to some obscure, illogical (British?) system of grading
#
# Author:      David
#
# Created:     09/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def grade_converter(n):
    if n >= 75:
        return "First"
    elif n >= 70 and n < 75:
        return "Upper Second"
    elif n >= 60 and n < 70:
        return "Second"
    elif n >= 50 and n < 60:
        return "Third"
    elif n >= 45 and n < 50:
        return "F1 Supp"
    elif n >= 40 and n < 45:
        return "F2"
    else:
        return "F3"

xs = [83,75,74.9,70,69.9,65,60,5939,55,50,49.9,45,44.9,40,39.9,2,0]

for x in xs:
    grade = grade_converter(x)
    print (x, "marks yields a grade of", grade)

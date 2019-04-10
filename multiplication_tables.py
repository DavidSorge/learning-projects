#-------------------------------------------------------------------------------
# Name:        Multiplication Tables
# Purpose:     Print Multiplication tables, 6x6
#
# Author:      David
#
# Created:     10/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def print_multiples(n, high):
    for i in range(1,high+1):
        print(n*i, end="\t")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i)

print_mult_table(9)

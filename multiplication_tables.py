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
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """



def print_multiples(n, high):
    for i in range(1,high+1):
        print(n*i, end="\t")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i)

print_mult_table(9)

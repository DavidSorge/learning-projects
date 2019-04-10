#-------------------------------------------------------------------------------
# Name:        Newton-Raphson method for Square Roots
# Purpose:     Apply an iterative algorithm to find the square root of n
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

def approx_equal(x,y):
    """tells you that two numbers are approximately equal if the are equivalent to 5 dp"""
    if abs(x-y) < 0.00001:
        return True
    else:
        return False

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(approx_equal(sqrt(25.0), 5.0))
    test(approx_equal(sqrt(49.0), 7.0))
    test(approx_equal(sqrt(81.0), 9.0))

def sqrt(n):
    """finds the square root of n to 3 decimal places"""
    approx = n/2.0      # Starts by guessing half of n
    counter = 0
    while True:
        counter += 1
        better = (approx + n/approx)/2.0
        if abs(approx-better) < 0.001:
            print("This calculation took {0} iterations".format(counter))
            return better
        approx = better

test_suite()
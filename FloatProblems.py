#-------------------------------------------------------------------------------
# Name:        Float Problems
# Purpose:     Demonstrate pitfalls of using float numbers with equality tests.
#
# Author:      David
#
# Created:     10/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def approx_equal(x,y):
    """tells you that two numbers are approximately equal if the are equivalent to 5 dp"""
    if abs(x-y) < 0.00001:
        return True
    else:
        return False

import math
a = math.sqrt(2.0)
print (a, a*a)
print (a*a == 2.0)
print (approx_equal(a*a, 2.0))
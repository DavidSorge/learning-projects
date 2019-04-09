#-------------------------------------------------------------------------------
# Name:        Revisiting Compound Interest
# Purpose:     Playing with Fruitful and Void Functions
#
# Author:      David
#
# Created:     05/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def final_amt(p,r,n,t):
    """
    Apply the compound interest formula to p
    to produce the final amount.
    """

    a = p * (1 + r/n) ** (n*t)
    return a        #This is what makes the function "fruitful"


# now that we have the function above, let us call it.

toInvest = float(input("How much do you want to invest?"))
fnl = final_amt(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)

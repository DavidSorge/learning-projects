#-------------------------------------------------------------------------------
# Name:        Compound Interest Equation
# Purpose:
#
# Author:      David
#
# Created:     02/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#principal = input("What is your initial investment?")   # defines initial investment
#p = float (principal)

p = 10000
r = 0.08                                        # defines annual nominal nterest rate
n = 12                                          # defines number of times the interest is compounded per year
time = input ("How many years will the money be compounded?") #defines number of years interest will be compounded
t = float (time)
amount = p * (1 + r/n)**(n * t)
print(amount)

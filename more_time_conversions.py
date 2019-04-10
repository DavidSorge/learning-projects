#-------------------------------------------------------------------------------
# Name:        6.9
# Purpose:     Fruitful Functions and Testing
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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)))
    test(day_name(day_num("Thursday")))
    test(day_num("Halloween") == None)
    test(day_add("Monday" , 4) == "Friday")
    test(day_add("Tuesday" , 0) == "Tuesday")
    test(day_add("Tuesday" , 14) == "Tuesday")
    test(day_add("Sunday" , 100) == "Tuesday")
    test(day_add("Sunday" , -1) == "Saturday")
    test(day_add("Sunday" , -7) == "Sunday")
    test(day_add("Tuesday" , -100) == "Sunday")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("Thermidor") == None)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)

def turn_clockwise(direction):
    """Takes a cardinal compass direction as its parameter,
and returns the next cardinal compass direction clockwise."""
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"

def day_name(n):
    """Converts an integer between 0 and 6 to a day of the week, Sunday = 0"""
    if n == 0:
        return ("Sunday")
    elif n == 1:
        return ("Monday")
    elif n == 2:
        return ("Tuesday")
    elif n == 3:
        return ("Wednesday")
    elif n == 4:
        return ("Thursday")
    elif n == 5:
        return ("Friday")
    elif n == 6:
        return ("Saturday")

def day_num(n):
    """Converts a day of the week to an integer between 0 and 6, Sunday = 0"""
    if n == "Sunday":
        return (0)
    elif n == "Monday":
        return (1)
    elif n == "Tuesday":
        return (2)
    elif n == "Wednesday":
        return (3)
    elif n == "Thursday":
        return (4)
    elif n == "Friday":
        return (5)
    elif n == "Saturday":
        return (6)

def day_add(day, delta):
    """ Tells you the day of the week delta nights after a given day"""
    int_day = day_num(day)          # changes day to an integer
    int_day = int_day + delta       # adds the number of nights
    int_day = int_day % 7           # eliminates all full weeks
    day = (day_name(int_day))       # converts integer to a day of the week
    return day

def days_in_month(month):
    if month == "January":
        return 31
    elif month == "February":
        return 28
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31

def to_secs(hrs,mins,secs):
    """Converts a given number of hrs, mins, and secs to seconds"""
    hrs = float(hrs)
    mins = float(mins)
    secs = float(secs)
    mins = mins + 60 * hrs  # converts hours to minutes, adds remaining minutes
    secs = secs + 60 * mins # converts minutes to seconds, adds remaining secs
    secs = int(secs)
    return secs

test_suite()        # Here is the call to run the tests
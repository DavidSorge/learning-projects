#-------------------------------------------------------------------------------
# Name:        What time will my alarm go off?
# Purpose:
#
# Author:      David
#
# Created:     02/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

current_time = input ("What time is it now (to the nearest hour)?")
c_t = int(current_time)
wait_duration = input("In how many hours would you like your alarm to go off?")
w_d = int(wait_duration)
alarm_time = (c_t + w_d) % 24
print("Your alarm will go off at", alarm_time, ":00")
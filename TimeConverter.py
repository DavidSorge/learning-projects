#-------------------------------------------------------------------------------
# Name:        Time Converter
# Purpose:     Convert a user-entered number of seconds to days, hours, minutes, and seconds
#
# Author:      David
#
# Created:     02/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

raw = input("How many seconds should I convert to days, hours, and minutes?")
r = (int(raw))      #converts input into an integer
rmins = r // 60     #defines rmins as the number of whole minutes in the raw input
sec = r % 60        #defines sec as the remaining number of seconds
rhrs = rmins // 60  #defines rhrs as the number of whole hours in the raw input
mins = rmins % 60   #defines mins as the remaining number of minutes
rdays = rhrs // 24  #defines rdays as the number of whole days in the raw input
hrs = rhrs % 24     #defines hrs as the remaining number of hours
yrs = rdays // 365  #defines yrs as the number of whole years in the raw input
days = rdays % 365  #defines days as the remaining number of days
print(raw, 'seconds is equivalent to ', yrs, ' years, ', days, ' days, ', hrs, ' hours, ', mins, ' minutes, and ', sec, 'seconds.')

#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      David
#
# Created:     10/04/2019
# Copyright:   (c) David 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

year_born = ("Paris Hilton", 1981)

celebs = [('Brad Pitt', 1981), ('Jack Nicholson', 1937), ('Justin Bieber', 1994)]

for (nm,yr) in celebs:
    if yr < 1980:
        print(nm)
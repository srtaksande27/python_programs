# -*- coding: cp1252 -*-
#Assignment14

#To check whether the year is leap or not


year = int(raw_input("Enter the year in YYYY format: "))

if year%4 == 0:
    print "{} is a leap year".format(year)
else:
    print "{} is not a leap year".format(year)
raw_input()

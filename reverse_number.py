# -*- coding: cp1252 -*-
#Assignment5

#WAP to reverse a given number.

number = input ("Enter a number to be reversed= ")
reverse = 0
while number != 0:

    reverse = reverse * 10
    reverse = reverse + number%10
    number = number/10


print "\n\n The reverse of the number = {}".format(reverse)



raw_input()

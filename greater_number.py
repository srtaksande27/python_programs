# -*- coding: cp1252 -*-
#Assignment10

#WAP to accept three inputs from the user and find the greatest number among 3 numbers.
#(Get three numbers from raw_input)

a= float (raw_input("Enter First number: "))
        
b= float (raw_input("Enter Second number: "))
        
c= float (raw_input("Enter Third number: "))

if (a>b) and (a>c):
        print "{} is greater than {} and {}".format(a,b,c)
elif (b>a) and (b>c):
        print "{} is greater than {} and {}".format(b,a,c)
else:
        print "{} is greater than {} and {}".format(c,a,b)
        


raw_input()

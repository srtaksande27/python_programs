#Python Assignment1

# WAP to swap the value of two variables in Python without using third variable

var1= input("Enter first variable= ")
var2= input("Enter second variable= ")

print "Values of variable 1 is '{}' and value of variable 2 is '{}' BEFORE swapping ".format(var1, var2)

var1= var1 + var2
var2= var1 - var2
var1= var1 - var2


print "Values of variable 1 is '{}' and value of variable 2 is '{}' AFTER swapping ".format(var1, var2)

raw_input()

import random

for i in range(1):
    value1 = random.randint(1, 6)
    print "First Dice value is : {} ".format(value1)

for i in range(1):
    value2 = random.randint(1, 6)
    print"Second Dice value is : {} ".format(value2)
    
    total =value1+value2
    
    print "Move {} spaces.".format(total)

    
if value1 == value2:
    print("DOUBLES! Roll Again!")

raw_input()

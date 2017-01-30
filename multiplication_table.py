# To get the multiplication Table

num = int(raw_input("Enter a number to get the multiplication table :"))

print "The multiplication table for {} is : ".format(num)
for i in range(1,11):
    print num,"X",i,"=",num*i

print "Press any key to exit."
raw_input()
    

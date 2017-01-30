# To check whether the input is palindrome or not

palin = raw_input("Enter a string or number:")

if palin == palin[::-1]:
    print "The given input {} IS a palindrome.".format(palin)

else:
    print "The given input {} IS NOT a palindrome.".format(palin)

print "Press any key to exit."
raw_input()

first = int(raw_input("Enter the first digit:"))
second = int(raw_input("Enter the digit digit:"))

def f(x):
    return x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0
if second>first:
    prime = filter(f, range(first, second))

    print " The List of prime numbers between {} and {} is \n {} \
    \n Number of PRIME NUMBERS FOUND is {} ".format(first, second, prime, len(prime))

    print "\nThe PRIME numbers between {} and {} are: ".format(first,second)
    for number in prime:
        print number
    
else:
    print "First Number {} should be LESS than Second Number {}".format(first, second)

print "Print any key to exit the program"

raw_input()

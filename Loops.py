"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""
def add5until100():
    x = 0
    while x < 100:
        x = x + 5
        print (x)
    print("It added five 20 times")    
print (add5until100())




"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""

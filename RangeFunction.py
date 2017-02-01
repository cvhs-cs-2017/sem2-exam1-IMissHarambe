"""Use the range function to print the numbers from 40 to 1 (backwards)"""
def heck(x):
    while x > 1:
        x = x - 1
        print (x)

#print(heck(41))

"""Repeat the exercise but count by 5's"""
def darn(x):
    while x > 1:
        x = x - 5
        print (x)

#print(darn(40))



"""Write a program that will count print first 10 multiples of (n) where n is
taken from user input.  Include necessary print statements."""
def tenmultiples(y):
    for y in range(10):
        y = y*10
        print(y)
print (tenmultiples(10))

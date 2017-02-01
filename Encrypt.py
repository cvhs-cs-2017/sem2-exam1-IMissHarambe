"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def nohaksheer(x):
    vowels = "AaEeIiOoUu"
    novowels = ""
    for y in x:
        if y == 'a':
            novowels = novowels + " "
        elif y == "A":
            novowels = novowels + " "
        elif y == "E":
            novowels = novowels + " "
        elif y == "e":
            novowels = novowels + " "
        elif y == "I":
            novowels = novowels + " "
        elif y == "i":
            novowels = novowels + " "
        elif y == "O":
            novowels = novowels + " "
        elif y == "o":
            novowels = novowels + " "
        elif y == "U":
            novowels = novowels + " "
        elif y == "u":
            novowels = novowels + " "
        else:
            novowels = novowels + y
    return novowels
#print(nohaksheer('Computer Science Makes the World go round but it doesn\'t make the world round itself!'))



"""Write an encryption code that you make up and run it for the variable NoVowels"""
def hakrssucc(string):
    newstring = ""
    for ch in string:
        a = ord(ch)
        a = a + 8
        newstring = newstring + chr(a)
    return newstring

print (hakrssucc("Computer Science Makes the World go round but it doesn't make the world round itself!"))

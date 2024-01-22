inputString = input("Enter a string: ")
lowerCase = ""
upperCase = ""

for char in inputString:
    if char.islower():
        lowerCase += char
    elif char.isupper():
        upperCase += char

shiftedString = lowerCase + upperCase
print(shiftedString)
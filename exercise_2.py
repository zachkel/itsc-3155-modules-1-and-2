inputString = input("Enter a string: ")
backwardsString = []
for i in range(len(inputString) - 1, -1, -1):
    backwardsString += inputString[i]

print(backwardsString)
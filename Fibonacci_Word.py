listofwords = []

firstletter = input("Enter the first letter: ")
secondletter = input("Enter the second letter: ")
currentletter = firstletter

for i in range(0, 10):
    listofwords.append(currentletter)
    currentletter = currentletter + secondletter
    secondletter = currentletter


print(listofwords)

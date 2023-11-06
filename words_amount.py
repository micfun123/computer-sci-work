# how many repeated workds
string = input("Enter a string: ")
words = string.split()
words_amount = len(words)
print("The amount of words is: ", words_amount)
words = set(words)
words_amount = len(words)
print("The amount of unique words is: ", words_amount)

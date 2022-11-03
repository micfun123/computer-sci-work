import random
solved = 0 #if solved set one

#colours
redterminalcolour = "\033[1;31m"
greenterminalcolour = "\033[1;32m"
yellowterminalcolour = "\033[1;33m"
whiteterminalcolour = "\033[1;37m"


print(whiteterminalcolour)

#get words
lines = open('words.txt').read().splitlines()
word = random.choice(lines)
word = word.replace(" ", "")
word = word.upper()
print(word)
#add to array
letters = []
for i in word:
    letters.append(i)	

displaylast = []

while solved == 0:
    user_inpute = input("Guess 5 letter words:\n")
    if len(user_inpute) < 5 or len(user_inpute) > 5:
        print(redterminalcolour + "Enter a 5 character words")
    else:
        user_inpute = user_inpute.upper()
        if user_inpute == word:
            print(greenterminalcolour + "Solved")
            solved = 1
        else:
            for i in user_inpute:
                if i in word:
                    possitioni = word.index(i)
                    if user_inpute[possitioni] == word[possitioni]:
                        print(greenterminalcolour + f"Letter {i} is in the right place")
                    else:
                        print(yellowterminalcolour + f"Letter {i} is in the word but wronge place")
                else:
                    print(redterminalcolour + f"Letter {i} is not in the word")
                
            print(whiteterminalcolour)
            print("\n")

            

print(whiteterminalcolour + "Thank you for playing")

   


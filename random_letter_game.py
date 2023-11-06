import random

# generate 5 random letters
letters = []
for i in range(5):
    letters.append(chr(random.randint(97, 122)))

users_word = input("Enter a word using the letters {} ".format(letters))
users_word = users_word.lower()


def score_word(word):
    score = 0
    # if the letter is in the word, add 1 to the score. if the use a letter thats not in the word remove 0
    for letter in word:
        if letter in letters:
            score += 1
            letters.remove(letter)
        else:
            return 0
    return score


print("Your score is {}".format(score_word(users_word)))

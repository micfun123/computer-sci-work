import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def game():
    lines = open('words.txt').read().splitlines()
    word = random.choice(lines)
    word = word.replace(" ", "")
    word = word.upper()
    currentstate = list("_"*len(word))
    guesses = []
    wrong = []
    tries = 0
    print("Welcome to Hangman!")
    print(" ".join(currentstate))

    while True:
        if tries == 6:
            print("You lose!")
            print("The word was", word)
            break
        guess = input("Guess a letter: ")
        guess = guess.upper()
        if guess in guesses:
            print("You already guessed that letter")
            continue
        guesses.append(guess)

        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    currentstate[i] = guess
            print(" ".join(currentstate))
            if "_" not in currentstate:
                print("You win!")
                break
        else:
            print("Incorrect!")
            tries += 1
            print(HANGMANPICS[tries])
            wrong.append(guess)
            print("Wrong guesses:", wrong)
            print(" ".join(currentstate))
            print("You have", 6-tries, "tries left")



game()

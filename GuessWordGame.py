#guess a word from your given dict game

import random

name = input("Enter your name : ")
print("Welcome " + name.title() + "!")

words = ['kitten', 'mouse', 'dog', 'parrot', 'hamster']
word = random.choice(words)

print("Its a game to guess a word. Lets start ", name.title())

guesses = ''
chances = 10

while chances > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char, " ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You guessed the word!")

        print("The word was " + word)
        break

    print()
    guess = input("guess a letter :")
    guesses += guess

    if guess not in word:
        chances -= 1

        print("wrong guess")
        print("You have " + str(chances) + " chances left")

        if chances == 0:
            print("You lost")




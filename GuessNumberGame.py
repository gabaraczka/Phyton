# gra w zgadnij liczbe GUESS THE NUMBER
import random

print("This is a guess the number game")

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

x=random.randint(lower, upper)
total_chances = 10
print("\n\t You have only ", total_chances, "chances to guess the number\n" )


count=0
flag = False

while count < total_chances:
    count += 1
    guess = int(input("Enter guess: "))

    if guess == x:
        print("Congrats! You guessed the number in ", count, " try!")
        flag = Truerue
        break
    elif x > guess:
        print("Sorry you guessed the number too low")
    elif x < guess:
        print("Sorry you guessed the number too high")

if not flag:
    print("\n The number is %d" % x)
    print("\t Better Luck Next time")

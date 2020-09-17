#####################################################
#                                                   #
#   game of searching or guessing a secret number   #
#   v1.1 - added top-score                          #
#                                                   #
#####################################################

import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

print("Hello. And welcome to secret number.")
with open("topscore.txt", "r") as score_file:
    top_score = int(score_file.read())
    print(f"Top player needed {top_score} attempts to guess it right.")
    print("Now it's your turn. Guess a number between 1 and 100.")

while guess != secret:
    if attempts == 0:
        guess = int(input("Your guess: "))
    else:
        guess = int(input("Your next gues: "))
    attempts += 1
    if guess < secret:
        print("Your guess is below the secret number.")
    if guess > secret:
        print("Your guess is above the secret number.")

print("Yeah. You found it. The secret number is " + str(secret) + ".")
print("You used " + str(attempts) + " guesses to get it right.")

if attempts < top_score:
    print("You were better and got on top.")
    with open("topscore.txt", "w") as score_file:
        score_file.write(str(attempts))

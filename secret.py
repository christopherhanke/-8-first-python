#
#
#
#
#

import random

secret = random.randrange(1, 100)
guess = 0
guesses = 0

print("Hello. Guess a number between 1 and 100.")

while guess != secret:
    guess = int(input("Your guess: "))
    guesses = guesses + 1
    if guess < secret:
        print("Your guess is below the secret number.")
    if guess > secret:
        print("Your guess is above the secret number.")

print("Yeah. You found it. The secret number is " + str(secret) + ".")
print("You used " + str(guesses) + " guesses to get it right.")
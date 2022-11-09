# Created On: 4/7/21
# Author: Todd G
# This program generates a random number, user inputs guess, tells user too high or too low, continues inputting guesses until correct.
import random

randomNum = random.randint(1, 100)

guess = int(input("Enter your guess: "))

while (guess != randomNum):
  if (guess>randomNum):
    print("Too high!")
  else:
    print("Too low!")
  guess = int(input("Enter your guess: "))

print("You are correct!")
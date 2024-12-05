from random import *
#computer picks a random number between 1 and 6
computerNumber = randint(1, 6)
#asks user to pick number between 1 and 6
userNumber = int(input("Guess a random number between 1 and 6: "))
#if the user number is equal to the computer number it will print you win, else you wrong
if userNumber == computerNumber:
  print("You guessed right")
else:
  print("You guessed wrong")

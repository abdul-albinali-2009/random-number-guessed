from random import *
computerNumber = randint(1, 6)
userNumber = int(input("Guess a random number between 1 and 6: "))
if userNumber == computerNumber:
  print("You guessed right")
else:
  print("You guessed wrong")
tries = 0
guess = 0
while guess != 6 and tries < 5:
  tries += 1
  guess = int(input("Guess the number: "))
if tries >= 5:
  print("You did not get it.")
if guess == 6:
  print("You got it!")
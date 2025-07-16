import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2
while total != 2:
  print("Nope!")
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  total = dice1 + dice2
print("You got a 2!")
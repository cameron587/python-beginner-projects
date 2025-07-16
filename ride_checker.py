height = int(input("How tall are you? "))
credits = int(input("How many credits do you have? "))
if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits < 10:
  print("You do not have enough credits and are not tall enough.")
elif height < 137:
  print("You are not tall enough to ride.")
elif credits < 10:
  print("You do not have enough credits to ride.")
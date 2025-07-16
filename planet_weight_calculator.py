weight = float(input("How many kilograms do you weigh "))
plan_num = int(input("What is your planet number "))
if plan_num == 1:
  rel_grav = 0.38
elif plan_num == 2:
  rel_grav = 0.91
elif plan_num == 3:
  rel_grav = 0.38
elif plan_num == 4:
  rel_grav = 2.53
elif plan_num == 5:
  rel_grav = 1.07
elif plan_num == 6:
  rel_grav = 0.89
elif plan_num == 7:
  rel_grav = 1.14
else:
  print("Invalid planet number")
  rel_grav = None

if rel_grav:
  dest_weight = weight * rel_grav
  print("Your weight on that planet is", dest_weight, "kg")
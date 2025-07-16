month = int(input("What month is it? (1-12) "))
if month in [1, 2, 3]:
  print("Winter 🌨️")
elif month in [4, 5, 6]:
  print("Spring 🌱")
elif month in [7, 8, 9]:
  print("Summer 🌻")
elif month in [10, 11, 12]:
  print("Autumn 🍂")
else:
  print("Invalid")
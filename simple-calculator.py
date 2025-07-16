title = " simple calculator"
print(title.title())
print(" ")

#choice for equation

print("What do you want to do? (1-4)")
print("1) +")
print("2) -")
print("3) x")
print("4) /")

print(" ")

choice = int(input("Your choice " ))

if choice > 4 :
  print ("Invalid choice")

else:

#numbers

 print(" ")

num1 = float(input("input your first number " ))

#calculations

if choice == 1:
  num2 = float(input("What do you want to add? "))
  result = num1 + num2
  print(" ")
  print("= ", result)

if choice == 2:
  num2 = float(input("What do you want to subtract? "))
  result = num1 - num2
  print(" ")
  print("= ", result)

if choice == 3:
  num2 = float(input("What do you want to multipy by? "))
  result = num1 * num2
  print(" ")
  print("= ", result)

if choice == 4:
  num2 = float(input("What do you want to divide by? "))
  result = num1 / num2
  print(" ")
  print("= ", result)
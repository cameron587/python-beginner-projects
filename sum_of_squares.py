number = int(input("Insert a number: "))
total = 0
for i in range(number + 1):
  square = i ** 2
  total += square
print(total)
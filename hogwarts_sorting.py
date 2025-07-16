#scores
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn    2) Dusk")
q1_answer = int(input("Enter your answer (1-2): "))
if q1_answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif q1_answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

print("When I am dead, I want people to remember me as:")
print("1) The Good
2) The Great
3) The Wise
4) The Bold")
q2_answer = int(input("Enter your answer (1-4): "))
if q2_answer == 1:
  Hufflepuff += 2
elif q2_answer == 2:
  Slytherin += 2
elif q2_answer == 3:
  Ravenclaw += 2
elif q2_answer == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

print("Which kind of instrument most pleases your ear?")
print("1) The violin
2) The trumpet
3) The piano
4) The drum")
q3_answer = int(input("Enter your answer (1-4): "))
if q3_answer == 1:
  Hufflepuff += 4
elif q3_answer == 2:
  Slytherin += 4
elif q3_answer == 3:
  Ravenclaw += 4
elif q3_answer == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print("Slytherin:", Slytherin)
print("Hufflepuff:", Hufflepuff)
print("Ravenclaw:", Ravenclaw)
print("Gryffindor:", Gryffindor)
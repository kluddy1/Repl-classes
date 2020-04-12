import random

try_counter = 0
a = input("What is your name?")


print("Hello", a)

sn = random.randint(1,100)
print(a , ",the number is between 1 and 100. Guess it!Only 5 goes!")
b = input("Your predictions?")
b = int(b)
try_counter = try_counter + 1
if b < sn:
  print("Too low!")
if b > sn:
  print("Too high!")
while b != sn and try_counter < 7:
  b = input("Your predictions?")
  try_counter = try_counter + 1
  b = int(b)
  if b < sn:
    print("Too low!")
  if b > sn:
    print("Too high!")
  if b == sn:
    print("Well done!!!")
  if b != sn and try_counter == 7:
    print("You lose!!!")
    print("The answer was", sn)

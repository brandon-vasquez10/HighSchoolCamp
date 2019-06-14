"""

title: loops_practice
author: Brandon
date: 2019-06-13 13:41
"""
for i in [89, 41, 73, 90]:
    print(i, end=" ")
print()
print("=" * 30)

for i in range(5, 15):
    print(i, end=" ")
print()
print("=" * 30)
for i in range(80, 31, -8):
    print(i, end=" ")
print()
print("=" * 30)

for i in range(3):
    print("alright", end=" ")
    print()
    print()


countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1

print('The countdown has ended')


x_input = int(input("Enter a number greater than 0: "))
while (x_input < 0):
  print("Waiting")
  x_input = input("Enter a number greater than 0: ")
print("Thank you for typing x!")
print()
print("=" * 30)

first = int(input("Enter a number: "))
second = int(input("Enter a second number: "))

while second < first:
    second = int(input("Invalid response. enter a second number"))

while first <= second:
    print(first)
    first += 1

x = input("Enter response ('Y', 'y', 'yes', 'YES' or 'n', 'no', 'NO'")

while x != 'Y' or x!= 'y' or x!= 'yes' or x!= 'YES' or x!= 'N':


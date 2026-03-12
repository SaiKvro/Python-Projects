#Question 1 
#Largest Number

largest_number = 0
a = 7
b = 12
c = 5

for i in range(a, b, c):
    if a > b and a > c:
        largest_number = a
    elif b > a and b > c:
        largest_number = b
    else:
        largest_number = c

print(f"The largest number is: {largest_number}")

#The loop is not needed and the program skips it anyway
#Here is the correct version

a = 7
b = 12
c = 5

if a >= b and a >= c:
    largest_number = a
elif b >= a and b >= c:
    largest_number = b
else:
    largest_number = c

print(f"The largest number is: {largest_number}")



#Question 2
#Count Even Numbers

count = 0

for i in range(1, 31):
    if i % 2 == 0:
        count += 1

print(f"There are {count} even numbers")

#100% correct



#Question 3
#Factorial Calculator

factorial = 1

for i in range(1, 6):
    factorial *= i

print(f"The factorial is: {factorial}")

#100% correct



#Question 4
#Number guessing simulation


secret_number = 8
guess = 3
attempts = 5

while guess != secret_number and attempts > 0:
    attempts -= 1
    print("Wrong guess")
else:
    print("Game over")

#Works correctly but could've been written cleaner

while guess != secret_number and attempts > 0:
    print("Wrong guess")
    attempts -= 1

if attempts == 0:
    print("Game Over")



#Question 5 Pattern Printer

character = "*"

for i in range(1, 6):
    print(character * i)

#100% correct


#Bonus challenge
#Sum of multiples of 3

total = 0

for i in range(1, 51):
    if i % 3 == 0:
        total = total + i

print(f"The total is: {total}")


#Score
#1 = 8/10
#2 = 10/10
#3 = 10/10
#4 = 8.5/10
#5 = 10/10
#6 = 10/10

#Overall
# 9.4/10

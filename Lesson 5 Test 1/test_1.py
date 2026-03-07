#Question 1 Number Analyzer

number = 6

if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#Question 1 completed but here is how it could have been improved
sign = ""
parity = ""

if number > 0:
    sign = "Positive"
elif number < 0:
    sign = "Negative"
else:
    sign = "Zero"

if number % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

print(f"The number is {sign}")
print(f"The number is {parity}")


#Question 2 Sum of Even numbers

total = 0

for i in range(1, 51):
    if i % 2 == 0:
        total += i
    
print(f"The sum of even numbers is: {total}")

#Question 2 passed but here is a more advanced way of completing it

for i in range(2, 51, 2):
    total += i

#Question 3 Password Attempts

correct_password = "python123"

attempts = 3

while correct_password != "python123" and attempts > 0:
    attempts = attempts - 1
    print("Wrong password")
if attempts == 0:
    print("Account locked")

#Question 3 not correct as the loop never starts due to wrong while statement
#Here is how it should've been written

correct_password = "python123"
user_password = "wrong"

attempts = 3

while user_password != correct_password and attempts > 0:
    print("Wrong password")
    attempts -= 1

if attempts == 0:
    print("Account locked")

#Question 4 Multiplication Table Generator

for i in range(1, 11):
    print(f"1 x {i} = {1 * i}")
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")
for i in range(1, 11):
    print(f"4 x {i} = {4 * i}")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#Question 4 could've been way cleaner
for num in range(1, 6):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

#Bonus challenge
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Bonus challenge is correct



#Points
#1 = 10/10
#2 = 9/10
#3 = 6.5/10
#4 = 6/10
#5 = 10/10

#Overall
# 8.3/10
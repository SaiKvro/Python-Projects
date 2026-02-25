#Exercise 1: Grading sysytem

score = 91

if score >= 90:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
else:
    print("Grade F")

#Cleaner way of completing exercise 1

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

#Exercise 2: Temperature Advice

temperature = 2

if temperature < 0:
    print("Freezing temperature")
elif 0 <= temperature <= 10:
    print("Cold temperature")
elif 11 <= temperature <= 25:
    print("Warm temperature")
else:
    print("Hot temperature")

#Cleaner way of completing exercise 2

if temperature < 0:
    print("Freezing")
elif 0 <= temperature <= 10:
    print("Cold")
elif 11 <= temperature <= 25:
    print("Warm")
else:
    print("Hot")

#Exercise 3: Simple calculator Logic
number_1 = 10
number_2 = 5

operation_1 = "+"
operation_2 = "-"
operation_3 = "*"
operation_4 = "/"

print(number_1, operation_1, number_2)
print(number_1, operation_2, number_2)
print(number_1, operation_3, number_2)
print(number_1, operation_4, number_2)

#Exercise 3 is supposed to make a calculation not print it
#Revised version

operation = "+"

if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
else:
    print("Invalid operation")


#Mini challenge: Leap Year Checker

year = 2000

if year % 4 == 0:
    if year / 100 != 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#Mini challenge revised

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year.")
    elif year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year")
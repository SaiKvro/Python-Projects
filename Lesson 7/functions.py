#Exercise 1
#Simple Function

def welcome():
    print("Welcome to Python!")

welcome()
welcome()
welcome()


#Exercise 2
#Function with Parameter



def square(number):
    number = number * number
    print(number)

square(4)

#Dont need to reassign number in exercise 2

def square(number):
    print(number * number)

square(4)

#Even better way of doing it

def square(number):
    return number * number

print(square(4))

#Exercise 3
#Function with Return



def multiply(a, b):
    return a * b

total = multiply(1, 5)
print(total)



#Exercise 4
#Even or Odd Function

def even_odd(number):
    if number % 2 == 0:
        return("Even")
    else:
        return("Odd")

result = even_odd(3)
print(result)

#Cleaner version of exercise 3

def even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

result = even_odd(3)
print(result)



#Mini Challenge
#Calculator Function

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return("Invalid Operation")

print(calculator(10, 5, "+"))


#Improvement to include division by 0

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return("Invalid Operation")

print(calculator(10, 5, "+"))
#Exercise 1
#Even or Odd

number = 11

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    



#Exercise 2
#Age category

age = 12

if age < 13:
    print("Child")
elif age >= 13 and age <= 17:
    print("Teen")
elif age >= 18:
    print("Adult")
else:
    print("Invalid choice")


#Cleaner way to complete exercise 2

age = 12

if age < 13:
    print("Child")
elif 13 <= age <= 17: #shorter way of writing this condition
    print("Teen")
else:
    print("Adult") #If the number is valid and previous 2 conditions are not met it means that the number must be 18 or over


#Exercise 3
#Password check

user_password = "python123"

if user_password == "python123":
    print("Access granted")
else:
    print("Access Denied")


#Mini challenge
#Number Comparison

number_1 = 4
number_2 = 7

if number_1 > number_2:
    print("Number 1 is bigger")
elif number_1 < number_2:
    print("Number 2 is bigger")
else:
    print("Numbers are equal")


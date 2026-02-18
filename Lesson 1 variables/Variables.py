#Exercise 1
print("Exercise 1")
name = "Sai"
age = 25
favorite_number = 4

print(name, age, favorite_number)



#Exercise 2
print("Exercise 2")
number_1 = 2
number_2 = 3

sum = number_1 + number_2
difference = number_1 - number_2
product = number_1 * number_2

print("Sum is :", sum)
print("Difference is :", difference)
print("Product is :", product)



#Exercise 3
print("Exercise 3")
a = 5
b = 10

a1 = b
b1 = a

a = a1
b = b1

print("A = ", a)
print("B = ", b)

#Easier way to complere exercise 3
a = 5
b = 10
5
a, b = b, a

print("A = ", a)
print("B = ", b)

#Mini Challenge
print("Mini Challenge")
print("Hello, my name is", name)
print("I am", age, " years old.")
print("My favorite number is", favorite_number)


#Updated way of printing using f-strings
print(f"Hello, my name is {name}.")
print(f"I am {age} years old")
print(f"My favourite number is {favorite_number}. ")
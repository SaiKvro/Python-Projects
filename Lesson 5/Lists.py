#Exercise 1
#Print all Items


numbers = [3, 8, 12, 7, 15]

for num in numbers:
    print(num)

#Exercise 2
#Sum of List
total = sum(numbers)

print(f"The sum is: {total}")



#Exercise 3
#Find the largest number

largest = 0
numbers = [4, 9, 2, 15, 6]

for i in numbers:
    if i > largest:
        largest = i

print(f"The largest number is {largest}")

#This code is correct in this case but if the list had any negative numbers the code would return 0 instead calculating the list contents
#Here is a better approcah that will work no matter the list contents

numbers = [4, 9, 2, 15, 6]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}")

#Even shorter way of doing it

largest = max(numbers)

print(f"The largest number is {largest}")



#Exercise 4
#Count even numbers

even = 0
numbers = [5, 8, 12, 3, 7, 10]

for i in numbers:
    if i % 2 == 0:
        even += 1


print(f"There are {even} even numbers in the list")

#Mini challenge
#Buuild a list
numbers = []

for i in range(1, 11):
    numbers.append(i)

print(numbers)

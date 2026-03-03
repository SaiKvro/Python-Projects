#Exercise 1 Print 1 to 10


for i in range(1, 11):
    print(i)


#Exercise 2 Sum of Numbers

count = 0
total = 0


for i in range(101):
    count = count + 1
    total = total + i
    if i == 101:
        break
    print(f"The sum is {total}")


#Simplified exercise 2

total = 0

for i in range(1, 101):
    total += i

print(f"The sum is {total}")

#Professional way for exercise 2

total = sum(range(1, 101))
print(total)



#Exercise 3 Multiplication Table

five_sum = 0

for i in range(1, 11):
      five_sum = 5 * i
      print(f"5 * {i} = {five_sum}")


#Clearner version of exercise 3
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


#Exercise 4 Countdown

count = 0
countdown = 11

while count < 11:
      count += 1
      countdown = countdown - 1
      print(countdown)
if countdown == 0:
      print("Blast Off!")


#Cleaner version of exercise 4

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast Off!")
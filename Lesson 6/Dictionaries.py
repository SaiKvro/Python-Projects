#Exercise 1 
#Create and access

student = {
    "name" : "John",
    "age" : 20,
    "grade" : "A"
}

print(student["name"])
print(student["grade"])



#Exercise 2
#Update Dictionary

student["age"] = 21
student["subject"] = "Math"

print(student)



#Exercise 3
#Loop through Dictionary

for key, value in student.items():
    print(key, ":", value)



#Exercise 4
#Count Items
count = 0

for key in student:
    count += 1

print(f"There are {count} items in the dictionary")

#Easier way of counting the items inside the dictionary

print(f"There are {len(student)} items in the dictionary")




#Mini Challenge
#Store Multiple People

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

#for key, value in people:
#    print(f"{key} is  {value} years old")



#People is a list of dictionaries not a dictionary therefor firstly you need to loop through a list and then access the dictionary

for person in people:
    print(f"{person["name"]} is {person["age"]} years old")

#Cleaner version

for person in people:
    name = person["name"]
    age = person["age"]
    print(f"{name} is {age} years old")



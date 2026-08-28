# example of sets
names = ["Anna", "Boris", "Anna", "Hanna", "Boris"]

unique_names = set(names)
print(unique_names)

#Exercise 11 — Set basics
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.add(3)
numbers.remove(2)
print(numbers)

#Exercise 12 — Remove duplicates with a set
names = [
    "Anna",
    "Boris",
    "Anna",
    "Hanna",
    "Boris",
    "David",
    "Hanna"
]
unique_names = set(names)
print(names)
print(unique_names)

#Exercise 13 — Set membership
languages = {"Python", "Java", "JavaScript", "Swift"}

print("Python" in languages)
print("C++" in languages)
print("Java" in languages)
print("Swift" in languages)
print("Ruby" in languages)

#Exercise 14 — Set mathematics
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a| b)
print(a & b)
print(a - b)
print(b - a)

# Exercise 16 — Choose the correct structure
students = ["Anna", "Boris", "Hanna",]
coordinates = (28.0001,23.9993,-91,2345)
student = {
    "name": "Jerry",
    "age": 30,
    "is_student": True

}

courses = {"Biology","Chemistry","Math"}

print(type(students))
print(type(coordinates))
print(type(student))
print(type(courses))
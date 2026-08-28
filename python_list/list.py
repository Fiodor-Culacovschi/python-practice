# list [] collection that I want to change
# Tuple () collection that should not change
#dict { key: information organized by key
# values}
# set {} / set () unique values

# example of a list
fruits = ["apple", "banana","orange"]
fruits[1] = "grapes"
fruits.append("cherry")
fruits.remove("apple")
fruits.pop(1)
print(fruits)
print (fruits[0])
print(fruits[-2])

print("********************************")

# A list can contain multiple data types
#person = ["Anna",25,5.7,True]

#exercise 1
#list
a = [1, 2, 3]
#tuple
b = (1, 2, 3)
#dict
c = {
    "name": "Anna",
    "age": 25
}
#set
d = {1, 2, 3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("********************************")

#exercise 2
fruits = ["apple", "banana","orange", "grape", "mango"]
print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-2])

print("********************************")

# Exercise 3
colors = ["red", "blue","green"]
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")
print(colors)

print("********************************")

# exercise 4
numbers = [10,20,10,30,20,40,10]

# 7 values are in the list
print(len(numbers))
# first value 10
print(numbers[0])
# last value 10
print(numbers[-1])
# 3 times value 10 appears in the list
print(numbers.count(10))
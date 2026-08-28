# list [] collection that I want to change
# Tuple () collection that should not change
#dict { key: information organized by key
# values}
# set {} / set () unique values

# tuple example
coordinates = (25.7,-80.2)
print(coordinates[0])
print(coordinates[1])

print("******************************")
# example of why tuples are immutable
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday")

# Exercise 5
coordinates = (28.5383, -81.3792)
print(coordinates[0])
print(coordinates[1])
print(type(coordinates))

# if we try to change tuple - this error will be displayed: "TypeError: 'tuple' object does not support item assignment", because tuples are immutable, values cannot be changed later 
coordinates[0] = 30.000
print(coordinates)

print("******************************")
# Exercise 6

list_data = [10, 20, 30]
tuple_data = (10, 20, 30)

#replacing first value of the list from 10 to 100
list_data[0] = 100
print(list_data)

#replacing first value in tuple from 10 to 100
# explanation same as above in exercise 5, this error will appear after we try to modify tuple: "TypeError: 'tuple' object does not support item assignment"
# errors means that we can't change, add values in tuple
tuple_data[0] = 100
print(tuple_data)
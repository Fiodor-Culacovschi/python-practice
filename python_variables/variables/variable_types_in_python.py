# indetify the type
a = 25
b = 14.7
c = "hello"
d = True
e = None 
f = "100"
g = 0 
h = -3.5
i = False
j = "False"

print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))
print (type(g))
print (type(h))
print (type(i))
print (type(j))

# choose the correct type 
first_name = "Anna"
age = 21
height = 6.7
number_of_cars = 2
is_employed = True
zip_code = "12345"
phone_number = "1234567890"
bank_account_balance = 3.75
bank_balance = "$3.75"
middle_name = None
current_temperature = 85.3

print("**************************")

print(type(first_name))
print(type(age))
print(type(height))
print(type(number_of_cars))
print(type(is_employed))
print(type(zip_code))
print(type(bank_account_balance))
print(type(bank_balance))
print(type(middle_name))
print(type(current_temperature))
print("*****************************")
print (bank_account_balance)
print(bank_balance)

print("*****************************")

# poor choice
age = "25"
number_of_students = 25.7
is_logged_in = "True"
telephone_number = 3055551234
middle_name = ""
price = "19.99"

print("Poor choice for variable 'age',because Python will read as string not as integer")
print("Poor choice for variable 'number_of_students',because Python will read as float not as integer")
print("Poor choice for variable 'is_logged_in',because Python will read as string not as boolean")
print("Poor choice for variable 'telephone_number',because Python will read as integer not as string")
print("Poor choice for variable 'middle_name',because Python will read as empty string not as NoneType")
print("Poor choice for variable 'price',because Python will read as string not float")


print("*****************************")

#predict the output exercise A
a = 40
b = 20
print ("This line of code will calculate two integers and display correct output " +str (a+b))


#exercise B
a = "10"
b = "20"
print ("This line prints variables as string it tis not wrong if is intended otherwise wrong "+ a+b)

# exercise C
z = 10
t = "20"
print ("Python will display this error: 'TypeError: unsupported operand type(s) for +: 'int' and 'str' ")
#print (z+t)

# exercise D
x = 10
y = 10.0
print(type(x))
print(type(y))
print(x==y)
# x and y have different data types:
# x -> int
# y -> float
# However, x == y compares their VALUES, not their types.
# 10 and 10.0 represent the same numerical value, so the result is True.


# exercise E

m = "123"
print(type(m))

m = int(m)
print(type(m))
print("In this case we converted 'str type into 'int' type")

# converting variables, exercise A convert into integer
age = "35"

age = int(age)
print(age)


#exercise B, convert into float
price = "19.99"

price = float(price)
print(price)

# exercise C, convert into string
number = 50

number = str(number)
print(number)
# exercise D, convert into integer
numbers = 15.8

numbers = int(15.8)

print(numbers)

# exercise , build a person profile
first_name = "Sarah"
last_name = "Down"
age = 19
height = 5.6
weight = 137.5
is_student = True 
middle_name = None 

print(type(first_name))
print(type(last_name))
print(type(age))
print(type(height))
print(type(weight))
print(type(is_student))
print(type(middle_name))


print("*****************************")

# exercise 7 important real-world challenge
# For each value below, decide whether it should be 'int', 'float', or 'str'
employee_number = "000123"
zipcode = "00501"
age = 30
price_tag = 25.99
product_quantity = 10
phone_number = "5551234567"
temperature = 72.4
credit_card_number = "41111111111111111"

print(type(employee_number))
print(type(zipcode))
print(type(age))
print(type(price_tag))
print(type(product_quantity))
print(type(phone_number))
print(type(temperature))
print(type(credit_card_number))

print("*****************************")

#exercise 8 debugging

# original wrong version
name = 123
age = "30"
height = "5.9"
is_employee = "False"
salary = "55000.75"

#correct version
name = "Alex"
age = 30
height = 5.9
is_employee = False
salary = 55000.75

print(type(name))
print(type(age))
print(type(height))
print(type(is_employee))
print(type(salary))

#exercise 9 challenge
#Create a small profile with exactly these six variables

name = "Dan"
age = 56
height = 6.3
is_student = True 
phone_number = "5671234589"

print(name)
print(type(name))

print(age)
print(type(age))

print(height)
print(type(height))

print(is_student)
print(type(is_student))

print(phone_number)
print(type(phone_number))

middle_name = None
print(middle_name)
print(type(middle_name))

print("--------------------")

middle_name = ""
print(middle_name)
print(type(middle_name))
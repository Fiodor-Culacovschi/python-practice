#if condition:
    # runs if True

#elif another_condition:
    # runs if first condition is False
    # and this condition is True

#else:
    # runs if all previous conditions are False

# and   both must be true
# or    at least one must be true
# not   reverses True/False

# in       exists inside collection
# not in   doesn't exist inside collection

# conditions examples
age = 20
if age >= 18:
    print("You are an adult")


print("*************************")
# another example
temperature = 90
if temperature >= 80:
    print("It is hot")

x = 10
if x == 10:
    print("x is 10")

# if + else
my_age = 16
if my_age >= 18:
    print("Adult")
else:
    print("Minor")

# if+elif+else
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

print("*************************")

math_score = 95
if math_score >= 70:
    print("C")
elif math_score >= 80:
    print("B")
elif math_score >= 90:
    print("A")


print("*************************")

# strings in conditions
username = "admin"
if username == "admin":
    print("Welcome admin")
else:
    print("You are not admin")

#Boolean variables in conditions
is_logged_in = False
if is_logged_in:
    print("Welcome")
else:
    print("Please log in")

    # using not, in this case it will prints "hello" because it reversing False
is_signed_in = False

if not is_signed_in:
    print("Hello")
else:
    print("Please sign in")


print("*************************")

# using and - means both conditions must be true
student_age = 25
is_student = True 

if student_age >= 18 and is_student:
    print("Adult student")


print("*************************")

# using or - at least one of the conditions has to be True
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

print("*************************")

# combining conditions
person_age = 25
is_pupil = True 
city = "Orlando"

if person_age >= 18 and is_pupil and city == "Orlando":
    print("Eligible")

# Membership with in, lists
print("*************************")

fruits = ["apple","banana","orange"]

if "apple" in fruits:
    print("Apple is available")

print("*************************")
# Membership with in, sets

allowed_roles = {"admin", "manager","employee"}

role = "admin"

if role in allowed_roles:
    print("Access allowed")

print("*************************")
# Membership with in, dictionaries

user ={
    "name": "Anna",
    "age": 25
}

if "name" in user:
    print("Name exists")

# nested conditions

son_age = 25
is_male = True 

if son_age >= 18:
    print("Adult")
if is_male:
    print("Adult student")

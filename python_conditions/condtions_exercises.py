# Exercise 1 — Basic if
#age = 25

#if age >= 18:
    #print("Adult")

# Exercise 2 — if/else
age = 16

if age > 18:
    print("Adult")
else:
    print("Minor")


# Exercise 3 — Positive, negative, zero
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("Zero")

# Exercise 4 — Grades
score = 87

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


print("*********************")

# Exercise 5 — Password

password = "Python123"
if password == "Python123":
    print("Access granted")
else:
    print("Access denied")

print("*********************")

# Exercise 6 — Boolean

is_logged_in = False
if is_logged_in:
    print("Welcome")
else:
    print("Please log in")

print("*********************")

# Exercise 7 — AND
my_age = 25
has_license = True 
if my_age >= 18 and has_license == True:
    print("You can drive")
else:
    print("You cannot drive")

print("*********************")

#  Exercise 8 — OR

day = "Sunday"
if day == "Saturday" or "Sunday":
    print("Weekend")
else:
    print("Weekday")

print("*********************")

# Exercise 9 — Membership
allowed_roles = {"admin","manager","employee"}

role = "admin"

if role in allowed_roles:
    print("Access granted")
else:
    print("Access denied")

print("*********************")

# Exercise 10 — List + condition
shopping_cart = ["milk", "bread", "eggs"]
if shopping_cart:
    print("Milk is in the cart")
else:
    print("Milk is not in the cart")

print("*********************")

# Exercise 11 — Dictionary + condition
user = {
    "name": "Anna",
    "age": 25,
    "is_active": True
}

if "is_active" in user:
    print("Account is active")
else:
    print("Account is inactive")

print("*********************")

# Exercise 12 — Data type + condition

another_age = 25

if type(another_age) == int:
    print("Age is an integer")
else:
    print("Age is not an integer")


print("*********************")
# Exercise 13 — Personal profile

name = "Alex"
person_age = 30
height = 5.9
is_student = False
phone_number = "5551234567"
middle_name = None 

if person_age >= 18:
    print("Adult")
else:
    print("Minor")
if is_student:
    print("Student")
else:
    print("Not a student")
if middle_name is None:
    print("No middle name")
else:
    print("Middle name exists")
if type(name) == str:
            print(type(name))
if type(person_age) == int:
    print(type(person_age))
if type(height) == float:
    print(type(height))
if type(is_student) == bool:
    print(type(is_student))

if type(phone_number) == str:
    print(type(phone_number))
if middle_name is None:
    print(type(middle_name))


print("*********************")

# Exercise 14 — Employee
employee = {
    "name": "Anna",
    "age": 32,
    "salary": 65000.50,
    "department": "IT",
    "is_manager": True

}

if employee["age"] >= 18:
    print("Employee is over 18")
if employee["department"] =="IT":
    print("Employee works in IT department")
if employee["is_manager"]:
    print("Employee is a manager")
if employee["salary"] > 60000:
    print("Salary is higher")


print("*********************")

# Exercise 15 — Shopping cart
cart = ["milk","bread", "eggs","cheese"]

if "milk" in cart:
    print("Milk exist in the cart")
else:
    print("Milk does not exist in the cart")
if "pizza" in cart:
    print("Pizza exist in the cart")
else:
    print("Pizza does not exist in the cart")
if "eggs" in cart:
    print("Eggs exist in the cart")
else:
    print("Eggs does not exist in the cart")

print("*********************")

# Exercise 16 — Allowed users
allowed_users = {"Anna","Boris","Hanna"}

username = "Boris"

if username in allowed_users:
    print("Username exists")
else:
    print("Username doesn't exists")
username = "David"
if username in allowed_users:
    print("Username exists")
else:
    print("Username doesn't exists")

print("*********************")

# Exercise 17 — Temperature
temperature = 85.5
if temperature < 40:
    print("Very cold")
elif temperature <= 59:
    print("Cold")
elif temperature <= 79:
    print("Comfortable")
elif temperature <= 99:
    print("Hot")
else:
    print("Very hot")

print("*********************")
# Exercise 18 — Login system
username = "admin"
password = "Python123"
is_active = True 

if username == "admin" and password == "Python123" and is_active:
    print("Login successful")
else:
    print("Login failed")

print("*********************")

# Exercise 19 — Product
product = {
    "name": "Laptop",
    "price": 999.99,
    "quantity": 5,
    "in_stock": True 
}

if product["in_stock"]:
    print("Product available")
else:
    print("Product is unavailable")
if product["quantity"] > 0:
    print("Items available")
else:
    print("Items unavailable")
if product["price"] < 1000:
    print("Affordable")
else:
    print("Expensive")
if "price" in product:
    print("Price exist as a key")
else:
    print("Price does not exist as a key")

print("*********************")

# Exercise 20 — The big Python challenge
# variables
visitor_name = "Dan"
visitor_age = 22
visitor_type = "Contractor"
is_approved = True 


# list
visitors_list = ["Dan","Sarah","Jean","Alex","Lucy"]
# tuple
location = (10,2)

# dictionary
visitor = {
    "visitor_name": "Dan",
    "visitor_age": 22,
    "visitor_type": "Contractor",
    "is_approved": True
}
# set
allowed_visitors = {"Guest","Contractor","Employee"}

# --- CONDITIONALS & LOGIC CHECKS ---
if visitor_age >= 18:
    print("Age requirement met: True")
else:
    print("Age requirement met: False")
if  visitor_type in allowed_visitors:
    print("Visitor type allowed: True")
else:
    print("Visitor type allowed: False")
if is_approved == True:
    print("Approved: True ")
else:
    print("Not approved")
if visitor_name in visitors_list:
    print("Visitor is on the visitor list")
else:
    print("Visitor is not on the list")
if "visitor_name" in visitor:
    print("Dictionary contains visitors' name")
else:
    print("It is not in the dictionary list")
if  type (location) is tuple:
    print("Building number found")
else:
    print("Building number not found")
if  type (location) is tuple:
    print("Floor number found")
else:
    print("Floor number not found")



print(f"Visitor: {visitor_name}")
print(f"Age: {visitor_age}")
print(f"Type: {visitor_type}")
print(f"Approved: {is_approved}")

print(f"Visitor type allowed: {is_approved}")
print(f"Age requirement met: {is_approved}")
print(f"Approved: {is_approved}")
if visitor_age >= 18 and visitor_type in allowed_visitors and is_approved == True:
    print("ACCESS GRANTED.")
else:
    print("ACCESS DENIED.")
#example of dictionaries
person = {
    "name": "Anna",
    "age": 25,
    "city": "Orlando"
}

print(person["name"])
print(person["age"])
print(person["city"])

# changing dictionary values
person = {
    "name": "Anna",
    "age": 26
}
print(person)

#adding dictionary value
person["job"] = "Developer"
print(person)

print("***************************")

# another dictionary example
user = {
    "username": "alex123",
    "age": 25,
    "email": "alex@example.com",
    "is_active": True
}
print(user)

# nested dictionaries
user = {
    "name": "Anna",
    "address": {
        "city": "Orlando",
        "state": "Florida",
        "zip": "32801"
    }
}

print(user["address"]["city"])

print("***************************")
#Exercise 7 — Dictionary creation

person ={
    "name": "Dan",
     "age": 23,
     "height": 6.3,
     "is_student": False,
     "city": "Tampa"
}

print(person)
print("***************************")

#Exercise 8 — Dictionary access

print(person["name"])
print(person["age"])
print(person["height"])
print(person["is_student"])
print(person["city"])

#Exercise 9 — Modify a dictionary
person = {
    "name": "Anna",
    "age": 25,
    "city": "Orlando"
}

person["age"] = 26
person["city"] = "Miami"
person["job"] = "Painter"
person["is_active"] = True

print(person)

#Exercise 10 — Dictionary challenge
employee = {
    "employee_id": "001",
    "name": "Alex",
    "department": "Sales",
    "salary": 1000,
    "is_manager": False

}
print(employee["employee_id"])
print(employee["name"])
print(employee["department"])
print(employee["salary"])
print(employee["is_manager"])

print(type(employee["employee_id"]))
print(type(employee["name"]))
print(type(employee["department"]))
print(type(employee["salary"]))
print(type(employee["is_manager"]))
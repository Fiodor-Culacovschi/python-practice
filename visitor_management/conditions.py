kinder_garten_age = 3
elementary_school_age = 6
miidle_school_age = 10
high_school_age = 16
number_a = 77
number_b = 77.0

colors = {"red","green", 12, True, 3.14}

if kinder_garten_age >= 1:
    print('Accepted by kindergarten')


if elementary_school_age >= 5:
    print("Ready to start elementary school")
else:
    print("Not ready for the school")

if miidle_school_age <= 7:
    print("Not ready for the middles school")
elif miidle_school_age >= 7:
    print("Ready to start middle school")

if high_school_age != 15:
    print("Not ready for the high school")
else:
    print("Ready for the high school")

if number_a and number_b == 77:
    print("Correct")
else:
    print("Incorrect")

if number_a or number_b != 77:
    print("Same numbers value")
else:
    print("Different numbers value")

if "red" not in colors:
    print("This color is not in the set list")
else:
    print("This color exists in the set list")

if 3.14 in colors:
    print(type(3.14))
else:
    print("Datatype not found")
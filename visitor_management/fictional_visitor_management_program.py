passenger_name = "Anna"
cabin_number = 103
space_suit_weight = 175.93
first_time_space_tourist = True 
luggage_items = ["Oxygen Tank","Moon Boots","Laser Camera"]

if space_suit_weight > 200:
    print("Please recalibrate the boots")
else:
    print("Weight is approved")

if not first_time_space_tourist:
    print("Welcome back")
else:
    print("First time in the space")

if "Laser Camera" not in luggage_items:
    print("Please verify your items")
else:
    print("All items are present")


print("\n")

print("Passenger name: " + passenger_name)
print(("Cabin number: "),cabin_number)
print(("Space-Suit Weight: "), space_suit_weight)
print(("First-Time Space Tourist: "), first_time_space_tourist)
print(("Luggage Items: " ), luggage_items)
print("\n")
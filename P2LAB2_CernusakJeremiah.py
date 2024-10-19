# Jeremiah Cernusak
# 09/30/2024
# P2LAB2
# Dictionary design and access


cars_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26,
}

mpg_values = cars_mpg.keys()
print(cars_mpg, "\n")

# user inputs desired vehicle 
user_model = input("Enter a vehicle to see its MPG:   ")
user_mpg = cars_mpg[user_model]


print("The", user_model, "will get", user_mpg, "miles per gallon.")

# user inputs amount of miles desired to travel
user_miles = int(input("How many miles will you drive the" + user_model + "?   "))

# divide miles driven by mpg to determine gallons of gas needed
gallons_needed = user_miles / user_mpg

# round down to nearest hundreth
gallons_needed = round(gallons_needed, 2)

print(f"You will need {gallons_needed} gallon(s) of gas to drive {user_miles} miles.")
# Jeremiah Cernusak
# 05 October 2024
# P2HW1
# Basic Math Calculator

print("Travel expense calculator. v0.02\n")

#starting amount input (b)
budget = float(input("Enter budget:  "))

#ask user for location of vacation (string)
destination = input("\nEnter your travel destination:  ")

#first number to be subtracted (x)
gasPrice = float(input("\nHow much are you spending on gas?  "))

#second number to be subtracted (y)
hotelPrice = float(input("\nHow much are you spending on living accomodations?  "))

#third number to be subtracted (z)
foodPrice = float(input("\nHow much are you spending on food?  "))

#calculation: final amount == b - (x + y + z)
finalAmount = float(budget - (gasPrice+hotelPrice+foodPrice))


# P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1
# P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1
# P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1 ----- P2HW1


budget = round(budget, 2)
gasPrice = round(gasPrice, 2)
hotelPrice = round(gasPrice, 2)
foodPrice = round(foodPrice, 2)
finalAmount = round(finalAmount, 2)

location_string = f"{'Location:':<25} {destination}"
initial_budget_string = f"{'Initial Budget:':<25} ${budget:.2f}"
gas_price_string = f"{'Fuel:':<25} ${gasPrice:.2f}"
hotel_price_string = f"{'Accomodation:':<25} ${hotelPrice:.2f}"
food_price_string = f"{'Food:':<25} ${foodPrice:.2f}"
final_amount_string = f"{'Remaining Balance:':<25} ${finalAmount:.2f}"


print("\n------------Travel Expenses------------")
print(f"{initial_budget_string}")
print(f"{gas_price_string}")
print(f"{hotel_price_string}")
print(f"{food_price_string}")
print("---------------------------------------\n")

print(f"{final_amount_string}\n\n\n")



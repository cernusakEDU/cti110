# Jeremiah Cernusak
# 17 September 2024
# P1HW2
# Basic Math Calculator

print("Travel expense calculator. v0.01\n")

#starting amount input (b)
budget = int(input("Enter budget:  "))

#ask user for location of vacation (string)
destination = input("\nEnter your travel destination:  ")

#first number to be subtracted (x)
gasPrice = int(input("\nHow much are you spending on gas?  "))

#second number to be subtracted (y)
hotelPrice = int(input("\nHow much are you spending on living accomodations?  "))

#third number to be subtracted (z)
foodPrice = int(input("\nHow much are you spending on food?  "))

#calculation: final amount == b - (x + y + z)
finalAmount = budget - (gasPrice+hotelPrice+foodPrice)


print("\n------------Travel Expenses------------\n\n")
print("Location:", destination)
print("Initial Budget:", budget,"\n")

print("Fuel:", gasPrice)
print("Accomodation:", hotelPrice)
print("Food:", foodPrice, "\n")

print("Remaining Balance: ", finalAmount)
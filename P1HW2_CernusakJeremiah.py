# Jeremiah Cernusak
# 17 September 2024
# P1HW2
# Basic Math Calculator

print("Travel expense calculator. v0.01\n")
budget = int(input("Enter budget:  "))
destination = input("\nEnter your travel destination:  ")

gasPrice = int(input("\nHow much are you spending on gas?  "))
hotelPrice = int(input("\nHow much are you spending on living accomodations?  "))
foodPrice = int(input("\nHow much are you spending on food?  "))

# pseudocode :: budget minus the sum of all the expenses
finalAmount = budget - (gasPrice+hotelPrice+foodPrice)


print("\n------------Travel Expenses------------\n\n")
print("Location:", destination)
print("Initial Budget:", budget,"\n")

print("Fuel:", gasPrice)
print("Accomodation:", hotelPrice)
print("Food:", foodPrice, "\n")

print("Remaining Balance: ", finalAmount)
# Jeremiah Cernusak
# 10/18/2024
# P3LAB
# Change Calculator

print("Coin change calculator. \n")

user_AmountInCents = float(input("Input the amount of money:    ")) * 100

dollars = user_AmountInCents // 100
user_AmountInCents %= 100
dollars = int(dollars)

quarters = user_AmountInCents // 25
user_AmountInCents %= 25
quarters = int(quarters)

dimes = user_AmountInCents // 10
user_AmountInCents %= 10
dimes = int(dimes)

nickels = user_AmountInCents // 5
user_AmountInCents %= 5
nickels = int(nickels)

pennies = user_AmountInCents // 1
pennies = int(pennies)

if dollars > 1:
    print(f"\n{dollars} dollars.")
elif dollars > 0:
    print(f"\n{dollars} dollar.")
if quarters > 1:
    print(f"{quarters} quarters.")
elif quarters > 0:
    print(f"{quarters} quarter.")
if dimes > 1:
    print(f"{dimes} dimes.")
elif dimes > 0:
    print(f"{dimes} dime.")
if nickels > 1:
    print(f"{nickels} nickels.")
elif nickels > 0:
    print(f"{nickels} nickel.")
if pennies > 1:
    print(f"{pennies} pennies. \n")
elif pennies > 0:
    print(f"{pennies} penny. \n")





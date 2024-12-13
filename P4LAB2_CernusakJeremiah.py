# Jeremiah Cernusak
# 11/03/2024
# P4LAB2
# Multiplication Table

# P4LAB2_LastnameFirstname.py

while True:
    user_input = int(input("Enter an integer: "))
    if user_input < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1, 13):
            print(f"{user_input} x {i} = {user_input * i}")

    run_again = input("Do you wish to run it again? ('yes'd / 'no'): ").lower()
    if run_again != "yes":
        break

print("Exiting program...")

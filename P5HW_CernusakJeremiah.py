# Jeremiah Cernusak
# 24 November 2024
# P5HW
# Math Quiz

import random

def main():
    while True:
        print("\nWelcome to Math Quiz")
        print("\nMAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")

        choice = input("\nPlease choose one of the menu options: ")

        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option from the menu.")

def addition():
    num1 = random.randint(1, 150)
    num2 = random.randint(1, 150)
    answer = num1 + num2
    guesses = 0

    print(f"\n  {num1}")
    print(f"+ {num2}")
    
    user_guess = -1
    while user_guess != answer:
        user_guess = int(input("\nYour answer: "))
        guesses += 1

        if user_guess == answer:
            print(f"\nCongratulations! You got it right in {guesses} guesses.")
        elif user_guess < answer:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

def subtraction():
    num1 = random.randint(151, 300)
    num2 = random.randint(1, 150)
    answer = num1 - num2
    guesses = 0

    print(f"\n  {num1}")
    print(f"- {num2}")
    
    user_guess = -1
    while user_guess != answer:
        user_guess = int(input("\nYour answer: "))
        guesses += 1

        if user_guess == answer:
            (f"\nCongratulations! You got it right in {guesses} guesses.")
        elif user_guess < answer:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

if __name__ == "__main__":
    main()

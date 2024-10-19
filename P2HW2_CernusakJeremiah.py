# Jeremiah Cernusak
# 12 October 2024
# P2HW2 
# Grade Analysis Tool

# 1. Prompt the user to enter grades for each module individually.
# 2. Store the entered grades in a list.
# 3. Calculate and display the lowest grade.
# 4. Calculate and display the highest grade.
# 5. Calculate and display the sum of all grades.
# 6. Calculate and display the average grade, formatted to two decimal places.

print("Grade analysis tool. \n")

# Ask user to enter grades for each module
grade01 = float(input("Enter grade for Module 1: "))
grade02 = float(input("Enter grade for Module 2: "))
grade03 = float(input("Enter grade for Module 3: "))
grade04 = float(input("Enter grade for Module 4: "))
grade05 = float(input("Enter grade for Module 5: "))
grade06 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades = [grade01, grade02, grade03, grade04, grade05, grade06]

print("\n---------Results---------")

# Display the grade info
print(f"\nLowest grade: {min(grades)}")  # Calculate and display the lowest grade
print(f"Highest grade: {max(grades)}")  # Calculate and display the highest grade
print(f"Sum of grades: {sum(grades)}")  # Calculate and display the sum of all grades
print(f"Average grade: {sum(grades)/len(grades):.2f}")  # Calculate and display the average grade, formatted to two decimal places

print("\n-------------------------")
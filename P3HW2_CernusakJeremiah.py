# Jeremiah Cernusak
# 10 / 19 / 2024
# P3HW2
# Employee Pay Calculator

# ✅ Asks the user to enter name of employee
# ✅ Ask user to enter number of hours the employee worked this week
# ✅ Ask user to enter employee's pay rate
# ✅ Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
# ✅ Calculate amount employee should be paid for regular hours worked.
# ✅ Display gross pay (total amount that should be paid to employee)
# ✅ The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).


# Print program title
print("Employee Pay Calculator \n")

# Prompt user to enter employee name
name = input("Enter employee name:  ")

# Prompt user to enter hours worked and convert to float
hours = float(input("Enter hours worked:  "))

# Prompt user to enter pay rate and convert to float
pay_rate = float(input("Enter pay rate:  "))

# Calculate overtime rate (1.5 times regular pay rate)
overtime_rate = pay_rate * 1.5

# Check if hours worked are greater than 40
if hours > 40:
    # Calculate overtime hours
    overtime_hours = round(hours - 40, 1)
    # Set standard hours to 40
    standard_hours = round(40, 1)
else:
    # No overtime, set overtime hours to 0
    overtime_hours = round(0, 1)
    # Set standard hours to hours worked
    standard_hours = round(hours, 1)

# Calculate standard pay and round to 2 decimal places
standard_pay = round(standard_hours * pay_rate, 2)

# Calculate overtime pay and round to 2 decimal places
overtime_pay = round(overtime_hours * overtime_rate, 2)

# Calculate gross pay (standard pay + overtime pay) and round to 2 decimal places
gross_pay = round(standard_pay + overtime_pay, 2)

print("\n----------------------------")
print(f"Employee name: {name}")
print("----------------------------\n")
print(f"Pay rate: ${pay_rate:.2f}")
print(f"Total hours worked: {hours:.1f}")
print(f"Overtime hours worked: {overtime_hours:.1f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Regular pay: ${standard_pay:.2f}")
print(f"Gross pay: ${gross_pay:.2f}\n")

# Jeremiah Cernusak
# 11/10/2024
# P4HW2
# Employee Pay Calculator

# Pseudocode
# 1. Initialize counters and accumulators to track the number of employees, as well as totals for overtime, regular, and gross pay.
# 2. Begin a loop that will continue until the user inputs "Done" as the employee’s name.
# 3. Within the loop:
#    - Request the employee's name.
#    - If the name is "Done", break out of the loop.
#    - Ask for the number of hours worked and the hourly pay rate.
#    - Determine overtime hours; if hours exceed 40, calculate the difference; otherwise, set overtime hours to zero.
#    - Calculate overtime pay by multiplying overtime hours by 1.5 times the hourly rate.
#    - For regular hours, if hours worked are over 40, set regular hours to 40; otherwise, set it to the hours worked.
#    - Find regular pay by multiplying regular hours by the hourly pay rate.
#    - Compute gross pay as the sum of regular pay and overtime pay.
#    - Display the employee's details in a structured table.
#    - Increase the employee count and add values to the running totals for overtime pay, regular pay, and gross pay.
# 4. After the loop ends, display the overall totals for all employees.


total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    name = input("Enter employee's name or 'Done' to terminate: ")
    
    if name == "Done":
        break

    hours_worked = input(f"How many hours did {name} work? ")
    hours_worked = float(hours_worked)  

    pay_rate = input(f"What is {name}'s pay rate? ")
    pay_rate = float(pay_rate) 

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
    else:
        overtime_hours = 0

    overtime_pay = overtime_hours * pay_rate * 1.5
    overtime_pay = round(overtime_pay, 2)

    if hours_worked > 40:
        regular_hours = 40
    else:
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate

    gross_pay = regular_pay + overtime_pay

    print(f"\nEmployee: {name}")
    print("------------------------------------------------------------")
    print("Hours Worked\tRate\tOvertime Hrs\tOvertime Pay\tRegular Pay\tGross Pay")
    print("------------------------------------------------------------")
    print(f"{hours_worked:.1f}\t\t{pay_rate:.2f}\t{overtime_hours:.1f}\t\t{overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}\n")

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

print("------------------------------------------------------------")
print(f"Total employees entered: {employee_count}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
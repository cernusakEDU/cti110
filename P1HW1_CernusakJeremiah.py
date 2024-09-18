import math
# The user should be able to enter any integer for the base value and
# the exponent. Then print the string showing the base, exponent, and 
# the result. Don't forget the exclamation points.

# Next, the user should enter three separate integers. The first two
# integers should be added together. Then the last given integer 
# should be subtracted from the sum of the other two numbers.


print("-----Calculating Exponenets---- \n\n")
baseValue = int(input("Enter an integer as the base value:  "))
exponenetValue = int(input("Enter an integer as the exponenet:  "))
solutionOne = pow(baseValue, exponenetValue)
print("\n\n", baseValue, " raised to the power of ", exponenetValue, "is ",solutionOne,"!!")

print("\n\n------Addition and Subtraction----\n\n")
numOne = int(input("Enter a starting integer: "))
numTwo = int(input("Enter an integer to add: "))
numThree = int(input("Enter an integer to subtract: "))
solutionTwo = numOne + numTwo - numThree
print("\n")
print(numOne, "+", numTwo, "-", numThree, "is equal to", solutionTwo)







# Jeremiah Cernusak
# 11/10/2024
# P4HW1
# Average Calculator v2

# 1. Ask the user how many scores they want to enter.
# 2. Create a list called 'user_scores' to store valid scores.
# 3. For each score:
#     - Ask the user to input a score.
#     - Validate the score to ensure it is between 0 and 100.
#     - If valid, add the score to 'user_scores'. If invalid, prompt the user again.
# 4. Once all scores are entered:
#     - Find the worst score entered.
#     - Remove the worst score from the 'user_scores' list.
#     - Calculate the average of the score list (after removing the lowest score).
#     - Determine the letter grade based on the average:
#         - A for average >= 90
#         - B for 80 <= average < 90
#         - C for 70 <= average < 80
#         - D for 60 <= average < 70
#         - F for average < 60
# 5. Display the worst score, the new score list, the average, and the letter grade.

print('Average Calculator. \n')

num_scores = int(input("Enter the number of scores you want to enter: "))

user_scores = []

for i in range(num_scores):
    while True: 
        score = int(input(f"Enter score {i+1}: "))
        if 0 <= score <= 100:
            user_scores.append(score)
            break 
        else:
            print("Invalid score! Please enter a score between 0 and 100.")


lowest_score = min(user_scores)

user_scores.remove(lowest_score)

average_score = sum(user_scores) / len(user_scores)

if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("\n-------Results-------")
print(f"Lowest score entered: {lowest_score}")
print(f"Score List after dropping the lowest score: {user_scores}")
print(f"Average of the modified score list: {average_score:.2f}")
print(f"Letter grade for the average: {letter_grade}")


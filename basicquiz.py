print("Welcome to the Basic Quiz!\n")
name = input("Enter your name: ")
print(f"\nHello, {name}!")
score = 0

# Question 1
answer1 = input("\n#1 What is the capital of Texas?\n ").lower()
if answer1 == "austin":
    print("Correct!")
    score += 1 # Gain 1 point
else:
    print("Wrong!")
    score -= 1 # Lose 1 point

# Question 2
try: # If user enters a word instead of number, invalid.
    answer2 = int(input("\n#2 What is 2x=12?\n "))
    if answer2 == 6:
        print("Correct!")
        score += 1 # Gain 1 point
    else:
        print("Wrong!")
        score -= 1 # Lose 1 point
except ValueError:
    print("Invalid input! You must enter a number.")

# Question 3
try: # If user enters a word instead of number, invalid.
    answer3 = int(input("\n#3 How many days are there in a week?\n "))
    if answer3 == 7:
        print("Correct!")
        score += 1 # Gain 1 point
    else:
        print("Wrong!")
        score -= 1 # Lose 1 point
except ValueError:
    print("Invalid input! You must enter a number.")

# Final Score
if score < 0:
    score = 0
print(f"\nYour final score is: {score}/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Keep practicing!")
else:
    print("Better luck next time.")

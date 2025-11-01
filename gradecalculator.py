#Grade calculator
score = int(input("Enter your score (0 -100):\n"))

if 0 <= score <= 100:
    if score >= 80 and score <= 100:
        grade = "A"
    elif score >= 70 and score < 80:
        grade = "B" 
    elif score >= 60 and score < 70:
        grade = "C"
    elif score >= 50 and score < 60:
        grade = "D"
    else:
        grade = "F"

    if grade == "F":
        print("You have failed the course.")
    else:
        print(f"Your grade is: {grade}, Congratulations! You Passed." )
else:
    print("Invalid score. Please enter a score between 0 and 100.")

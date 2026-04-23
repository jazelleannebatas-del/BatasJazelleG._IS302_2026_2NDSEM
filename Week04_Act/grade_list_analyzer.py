print("----- GRADE LIST ANALYZER -----")
grades_jab = []

# Ask user to enter 5 grades
for i_jab in range(1, 6):
    grade_jab = float(input(f"Enter grade {i_jab}: "))
    grades_jab.append(grade_jab)

# Compute statistics
average_grade_jab = sum(grades_jab) / len(grades_jab)
highest_grade_jab = max(grades_jab)
lowest_grade_jab = min(grades_jab)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_jab)
print("Average Grade:", round(average_grade_jab, 1))
print("Highest Grade:", highest_grade_jab)
print("Lowest Grade:", lowest_grade_jab)

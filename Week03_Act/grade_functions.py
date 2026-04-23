def calculate_average(grade1_jab, grade2_jab, grade3_jab):
    """Calculate the average of three grades"""
    return (grade1_jab + grade2_jab + grade3_jab) / 3

def get_remark(average_jab):
    """Return the remark based on the average grade"""
    if average_jab >= 90:
        return "Excellent"
    elif average_jab>= 85:
        return "Very Good"
    elif average_jab >= 80:
        return "Good"
    elif average_jab >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name_jab = input("Enter student name: ")
grade1_jab = float(input("Enter first grade: "))
grade2_jab= float(input("Enter second grade: "))
grade3_jab = float(input("Enter third grade: "))

# Calculate average and get remark
average_jab = calculate_average(grade1_jab, grade2_jab, grade3_jab)
remark_jab = get_remark(average_jab)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name_jab)
print("Grade 1:", grade1_jab)
print("Grade 2:", grade2_jab)
print("Grade 3:", grade3_jab)
print("Average:", round(average_jab, 2))
print("Remark:", remark_jab)

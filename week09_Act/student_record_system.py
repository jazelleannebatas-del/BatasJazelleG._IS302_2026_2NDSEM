name_jab = input("Enter student name: ")
course_jab = input("Enter course: ")
with open("students.txt", "a") as file_jab:
    file_jab.write(name_jab + "," + course_jab + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_jab:
    for line_jab in file_jab:
        print(line_jab.strip())

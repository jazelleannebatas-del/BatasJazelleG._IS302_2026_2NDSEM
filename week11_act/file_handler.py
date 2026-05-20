STUDENT_FILE_JAB = "students.txt"


def save_student_jab(student_jab):
    """Append a new student record to students.txt."""
    try:
        with open(STUDENT_FILE_JAB, "a") as file_jab:
            file_jab.write(student_jab.to_record())

    except Exception as error_jab:
        print("Error saving student:", error_jab)


def view_students_jab():
    """Display all student records from students.txt."""
    try:
        with open(STUDENT_FILE_JAB, "r") as file_jab:
            records_jab = [
                line_jab.strip()
                for line_jab in file_jab
                if line_jab.strip()
            ]

        if not records_jab:
            print("No records found.")
            return

        for record_jab in records_jab:
            try:
                student_id_jab, name_jab, course_jab = (
                    record_jab.split(",", 2)
                )

                print(student_id_jab, name_jab, course_jab)

            except ValueError:
                print("Skipped invalid record:", record_jab)

    except FileNotFoundError:
        print("No records found.")


def find_student_jab(student_id_jab):
    """Search for a student by ID and return the found record."""
    try:
        with open(STUDENT_FILE_JAB, "r") as file_jab:
            for line_jab in file_jab:
                if not line_jab.strip():
                    continue

                try:
                    stored_id_jab, name_jab, course_jab = (
                        line_jab.strip().split(",", 2)
                    )

                except ValueError:
                    continue

                if stored_id_jab == student_id_jab:
                    return stored_id_jab, name_jab, course_jab

    except FileNotFoundError:
        return None

    return None

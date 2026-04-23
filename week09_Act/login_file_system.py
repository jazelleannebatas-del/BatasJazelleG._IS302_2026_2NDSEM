def register_jab():
    username_jab = input("Enter username: ")
    password_jab= input("Enter password: ")
    with open("users.txt", "a") as file_jab:
        file_jab.write(username_jab + "," + password_jab + "\n")
    print("Registration successful!")

def login_jab():
    username_jab = input("Enter username: ")
    password_jab = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_jab:
            for line_jab in file_jab:
                stored_user_jab, stored_pass_jab = line_jab.strip().split(",")
                if username_jab == stored_user_jab and password_jab == stored_pass_jab:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_jab():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_jab = input("Enter choice: ")
        
        if choice_jab == "1":
            register_jab()
        elif choice_jab == "2":
            login_jab()
        elif choice_jab == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_jab()
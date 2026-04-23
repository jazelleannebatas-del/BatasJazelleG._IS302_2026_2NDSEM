correct_username_jab = "admin"
correct_password_jab = "1234"
attempts_jab= 0
while attempts_jab < 3:
    username_jab = input("Enter username: ")
    password_jab = input("Enter password: ")
    if username_jab== correct_username_jab and password_jab == correct_password_jab:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_jab += 1
if attempts_jab == 3:
    print("Account Locked")

CORRECT_PASSWORD = "Secret123"  # change this to whatever password you want

attempts = 0
password_correct = False

while attempts < 3 and not password_correct:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        password_correct = True
        print("Login successful. Welcome!")
    else:
        attempts += 1
        print(f"Incorrect password. Attempt {attempts} of 3.")

if not password_correct:
    print("Too many failed attempts. Your account has been locked.")
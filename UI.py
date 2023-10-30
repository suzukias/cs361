USER_LISTS = "users.txt"


def welcome_message():
    print("\nWelcome to your Expense Tracker! \nThis is your personal expense management service. You can easily track and manage your expenses.")


def login_or_signup():
    while True:
        selection = input(
            "\nPlease Register or Login by making a selection and pressing Enter.\n0 - Exit\n1 - Registration\n2 - Login\n3 - Help\nSelection: ")
        if selection == "0":
            exit()
        elif selection == "1":
            registration()
        elif selection == "2":
            login()
            return
        elif selection == "3":
            print("help page")
        else:
            print("Please select correct number.")


def get_registered_users():
    registered_users = []
    with open("users.txt", "r") as file:
        for line in file:
            username, _ = line.strip().split(',', 1)
            registered_users.append(username)
    return registered_users


def password_checker(password):
    if len(password) == 6:
        for char in password:
            if char.isdigit():
                return True
    return False


def registration():
    print("\nREGISTRATION PAGE\nPlease complete the following to register or make a selection and press Enter.\n0 - Exit\n1 - Back")
    username = input("Please enter a username: ")
    if username == "0":
        exit()
    elif username == "1":
        login_or_signup()
    else:
        registered_users = get_registered_users()
        if username in registered_users:
            print(
                f"Username {username} already exists. Please login to continue.")
        else:
            print(
                f"Username {username} is valid! \nNext, please enter your password. \nYour password must be 6 characters long and at least 1 number.")

            while True:
                password = input("Please enter a new password: ")
                if password_checker(password):
                    confirmation = input(
                        "Please enter your password again for confirmation: ")
                    if password == confirmation:
                        with open("users.txt", "a") as file:
                            file.write(f"{username},{password}\n")
                        print("Registration successful! Please login to continue.")
                        break
                    else:
                        print("Passwords do not match. Please try again.")
                else:
                    print(
                        "Password is invalid. It must be 6 characters long and contain at least 1 number.")


def login():
    print("\nLogin PAGE\nPlease complete the following to login or make a selection and press Enter.\n0 - Exit\n1 - Back to Top")
    username = input("Please input your username to login: ")
    if username == "0":
        exit()
    elif username == "1":
        login_or_signup()
    else:
        registered_users = get_registered_users()
        if username in registered_users:
            password = input("Please enter your password: ")
            password_matched = False
            with open("users.txt", "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(',', 1)
                    if username == stored_username and password == stored_password:
                        print("Login successful!")
                        password_matched = True
                        top_page()
                        break
            if not password_matched:
                print(
                    "Invalid password. Your password is 6 characters long and contains at least 1 number.")
                retry = input(
                    "\nDo you want to try login again?\n0 - Exit\n1 - Back to Top\n2 - Try Again\nSelection: ")
                if retry == "0":
                    exit()
                elif retry == "1":
                    login_or_signup()
                elif retry == "2":
                    login()
                else:
                    print(
                        "Invalid input. Please register or login again to use the service.")
                    login_or_signup()
        else:
            print("Username not found. Please register or try again.")
            login_or_signup()


def top_page():
    print("work in progress")


def main():
    welcome_message()
    login_or_signup()


if __name__ == "__main__":
    main()

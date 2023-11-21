import requests
import json


def welcome_message():
    print("\nWelcome to your Expense Tracker! \nThis is your personal expense management service. You can easily track and manage your expenses.")


def login_or_signup():
    while True:
        selection = input(
            "\nPlease Register or Login by making a selection and pressing Enter.\n0 - Exit\n1 - Registration\n2 - Login\n3 - Login Help\nSelection: ")
        if selection == "0":
            exit()
        elif selection == "1":
            registration()
        elif selection == "2":
            login()
            return
        elif selection == "3":
            login_help()
        else:
            print("Please select correct number.")


def login_help():
    print("\nLogin Help\nLogin is required to use this service.\nYour username can consist of numbers, letters, or a combination of both.\nYour password must be 6 characters long and at least 1 number.\nIf you have already registered, please go to login page and enter your username and password to use the service\nIf you don't have username and password, please go to register page to register.")
    selection = input(
        "\nPlease Register or Login by making a selection and pressing Enter.\n0 - Exit\n1 - Registration\n2 - Login\nSelection: ")
    if selection == "0":
        exit()
    elif selection == "1":
        registration()
    elif selection == "2":
        login()
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
                        home()
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


def home():
    print("\nHome\nPlease make a selection and press Enter.\n0 - Exit\n1 - View Your Expense\n2 - Enter Your Expense Log\n3 - Help")
    selection = input("Your selection: ")
    if selection == "0":
        exit()
    elif selection == "1":
        view_expense()
    elif selection == "2":
        enter_expense()
    elif selection == "3":
        service_help()
    else:
        print("Invalid input. Please select the correct number.")


def enter_expense():
    while True:
        print("\nEnter Your Expense Log\nPlease complete the following to log your expense or enter 0 to go back Home.\n0 - Back to Home")
        expense = input("Please input how much money did you spend: $")
        if expense == "0":
            home()
            break
        else:
            if not is_float(expense):
                print("Invalid input. Please enter a valid expense amount.")
            else:
                date = input("Date (YYYY-MM-DD): ")
                description = input("Description: ")
                with open("expenses.txt", "a") as file:
                    file.write(f"{date},{expense},{description}\n")
                print("Expense logged successfully!")
                home()
                break


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def view_expense():
    prices = read_expense_file()
    data = {"data": prices}
    url = 'http://localhost:3000/calculate'

    # Making a POST request
    response = requests.post(url, json=data)
    result = response.json()
    print(f"\nYour Total Expense: ${result['total']}")
    print(f"Your Average Expense: ${result['avg']}")
    print(f"Most Expensive Expense: ${result['max']}")
    print(f"Cheapest Expense: ${result['min']}")

    while True:
        selection = input(
            "\nWould you like to see all the expense history?\n0 - No (Back to Top)\n1 - Yes\nSelection: ")
        if selection == "0":
            home()
        elif selection == "1":
            with open("expenses.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(',')
                    date = parts[0]
                    price = parts[1]
                    price = float(price)
                    details = parts[2]
                    print(f"Date: {date} Amount: {price} Details: {details}")
                home()
                break
        else:
            print("Invalid input. Please select the correct number.")


def read_expense_file():
    prices = []
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(',')
            price = parts[1]
            price = float(price)
            prices.append(price)
    return prices


def service_help():
    print("work in progress")


def main():
    welcome_message()
    login_or_signup()


if __name__ == "__main__":
    main()

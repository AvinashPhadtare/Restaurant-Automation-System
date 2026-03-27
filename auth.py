import hashlib
from dotenv import load_dotenv
import os
import menu   

load_dotenv()

USER_FILE = "data/users.txt"


# ---------- PASSWORD HASH ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------- ADMIN PANEL ----------
def admin_panel():
    admin_password = os.getenv("ADMIN_PASSWORD")
    entered = input("Enter Admin Password: ")

    if entered != admin_password:
        print("Authentication Failed")
        return

    print("\n1. Login\n2. Add New User")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input")
        return

    if choice == 1:
        login()
    elif choice == 2:
        add_new_user()
    else:
        print("Wrong choice")


# ---------- ADD USER ----------
def add_new_user():
    username = input("Enter new username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    # prevent duplicate users
    try:
        with open(USER_FILE, "r") as f:
            for line in f:
                stored_user = line.split(":")[0]
                if username == stored_user:
                    print("User already exists")
                    return
    except FileNotFoundError:
        pass

    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hashed}\n")

    print("User added successfully")


# ---------- LOGIN ----------
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    try:
        with open(USER_FILE, "r") as f:
            users = f.readlines()
    except FileNotFoundError:
        print("No users found")
        return

    for user in users:
        stored_user, stored_pass = user.strip().split(":")

        if username == stored_user and hashed == stored_pass:
            print("Login successful")
            admin_dashboard()   # 👈 FIXED
            return

    print("Invalid username or password")


# ---------- ADMIN DASHBOARD ----------
def admin_dashboard():
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. Add Menu")
        print("2. View Menu")
        print("3. Logout")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            add_menu()

        elif choice == 2:
            menu_data = menu.load_menu()
            menu.show_menu(menu_data)

        elif choice == 3:
            print("Logged out")
            break

        else:
            print("Wrong choice")


# ---------- ADD MENU ----------
def add_menu():
    while True:
        dish = input("Enter dish name (or 'quit'): ")

        if dish.lower() == "quit":
            break

        try:
            price = float(input(f"Enter price for {dish}: "))
        except ValueError:
            print("Invalid price")
            continue

        # prevent duplicate dish
        menu_data = menu.load_menu()
        if dish.lower() in menu_data:
            print("Dish already exists")
            continue

        with open("data/menu.txt", "a") as f:
            f.write(f"{dish}:{price}\n")

        print("Dish added")
import hashlib
from dotenv import load_dotenv
import os
import menu   
load_dotenv()
USER_FILE = "data/users.txt"
MENU_FILE = "data/user.txt"



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
    else:
        login()



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
            admin_dashboard()   
            return

    print("Invalid username or password")



# ---------- ADMIN DASHBOARD ----------
def admin_dashboard():
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. Add Menu")
        print("2. View Menu")
        print("3. Add User")
        print("4. View User")
        print("5. Remove User")
        print("6. Delete Item")
        print("7. Update Price")
        print("8. Logout")

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
            add_new_user()

        elif choice == 4:
            show_user()

        elif choice == 5:
            remove_user()

        elif choice == 6:
            delete_item()

        elif choice == 7:
            update_price()

        elif choice == 8:
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

        with open(MENU_FILE, "a") as f:
            f.write(f"{dish}:{price:.2f}\n")

        print("Dish added")



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



# ---------- ADD USER ----------
def remove_user():
    try:
        username = input("Enter username to remove: ")

        with open(USER_FILE, "r") as f:
            users_details = f.readlines()

        with open(USER_FILE, "w") as f:
            for item in users_details:
                name, password = item.strip().split(":")
                if name.lower() != username.lower():
                    f.write(item)

        print("User deleted.")
    except:
        raise Exception(f"{username} is not in list of users.")



# ---------- DELETE ITEM ----------
def delete_item():
    try:
        name_to_delete = input("Enter item name to delete: ")

        with open(MENU_FILE, "r") as f:
            items = f.readlines()

        with open(MENU_FILE, "w") as f:
            for item in items:
                name, price = item.strip().split(":")
                if name.lower() != name_to_delete.lower():
                    f.write(item)

        print("Item deleted.")
    except:
        raise Exception(f"{name_to_delete} is not in Menu")



# ---------- UPDARE PRICE ----------
def update_price():
    try:
        name_to_update = input("Enter item name: ")
        new_price = float(input("Enter new price: "))
        with open(MENU_FILE, "r") as f:
            items = f.readlines()

        with open(MENU_FILE, "w") as f:
            for item in items:
                name, price = item.strip().split(":")
                if name.lower() == name_to_update.lower():
                    f.write(f"{name}:{new_price:.2f}\n")
                else:
                    f.write(item)

        print("Price updated.")
    except :
        raise Exception("Some Error Occured")



# ---------- LOAD MENU ----------
def show_user():
    try:
        with open(USER_FILE, "r") as f:
            names = f.readlines()
        print("\n----- USERNAME -----\n")
        for name in names:
            name, price = name.strip().split(":")
            print(name)
    except FileNotFoundError:
        print("User file not found")


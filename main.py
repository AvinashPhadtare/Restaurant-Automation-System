import auth
import menu
import orders

def main():
    while True:
        print("\n===== Welcome To Resto =====")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

        try:
            choice = int(input("Enter Your Choice (1-3): "))
        except ValueError:
            print("Invalid input. Enter number only.")
            continue

        if choice == 1:
            customer_dashboard()

        elif choice == 2:
            auth.admin_panel()

        elif choice == 3:
            print("Exiting... Thank You!")
            break

        else:
            print("Wrong choice. Try again.")


# ---------- CUSTOMER DASHBOARD ----------
def customer_dashboard():
    print("\n--- Customer Dashboard ---")

    menu_data = menu.load_menu()

    if not menu_data:
        print("Menu not available")
        return

    menu.show_menu(menu_data)
    orders.place_order(menu_data)
    


# ---------- RUN ----------
if __name__ == "__main__":
    main()
MENU_FILE = "data/menu.txt"


# ---------- LOAD MENU ----------
def load_menu():
    menu_dict = {}

    try:
        with open(MENU_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    name, price = line.strip().split(":")
                    menu_dict[name.lower()] = float(price)
    except FileNotFoundError:
        print("Menu file not found")

    return menu_dict


# ---------- SHOW MENU ----------
def show_menu(menu):
    if not menu:
        print("Menu is empty")
        return

    print("\n----- MENU -----")

    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item.capitalize():<10} : ₹{price:.2f}")
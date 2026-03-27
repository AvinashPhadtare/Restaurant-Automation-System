def place_order(menu):
    total = 0
    order_items = {}

    while True:
        item = input("\nEnter item name: ").lower()

        if item in menu:
            total += menu[item]
            order_items[item] = menu[item]
            print(f"{item} added. Price: ₹{menu[item]}")
        else:
            print("Item not available")

        another = input("Add more? (yes/no): ").lower()

        if another == "no":
            break
        elif another != "yes":
            print("Invalid choice")

    print("\n----- BILL -----")
    for i,item, price in order_items.items():
        print(f"{i}. {item.capitalize():<10} : ₹{price:.2f}")

    print(f"\nTotal Bill = ₹{total}")
    print("Thank You for your order!")
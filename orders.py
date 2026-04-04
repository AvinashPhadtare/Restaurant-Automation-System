from payment import process_payment


def place_order(menu):
    order_items = {}

    while True:
        item = input("\nEnter item name: ").lower()

        if item in menu:
            try:
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Quantity must be positive")
                    continue
            except ValueError:
                print("Invalid quantity")
                continue

            if item in order_items:
                order_items[item]["qty"] += qty
            else:
                order_items[item] = {
                    "price": menu[item],
                    "qty": qty
                }

            print(f"{item} x{qty} added. Price: ₹{menu[item] * qty}")

        else:
            print("Item not available")

        while True:
            another = input("Add more? (yes/no): ").lower()
            if another in ["yes", "no"]:
                break
            print("Invalid choice")

        if another == "no":
            break

    if not order_items:
        print("\nNo items ordered.")
        return

    print("\n----- BILL -----")

    total = 0
    for i, (item, details) in enumerate(order_items.items(), 1):
        price = details["price"]
        qty = details["qty"]
        subtotal = price * qty
        total += subtotal

        print(f"{i}. {item.capitalize():<10} x{qty} : ₹{subtotal:.2f}")

    print(f"\nTotal Bill = ₹{total:.2f}")


    # 🔥 PAYMENT INTEGRATION
    payment_success = process_payment(total, order_items)

    if payment_success:
        print("Order Confirmed ✅")
        print("Thank You for your order!")
    else:
        print("Order Cancelled ❌")
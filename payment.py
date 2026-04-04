import qrcode
import uuid
import os
from dotenv import load_dotenv
from whatsapp import send_whatsapp

load_dotenv()

ORDER_FILE = "data/orders.txt"


# ---------- GENERATE QR ----------
def generate_qr(amount):
    upi_id = os.getenv("UPI_ID")
    name = os.getenv("NAME")

    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.make(upi_url)
    qr.save("payment_qr.png")

    print("\nQR Code generated as payment_qr.png")

    try:
        os.startfile("payment_qr.png")
    except Exception as e:
        print("Error opening QR:", e)




        
    # ---------- PROCESS PAYMENT ----------
def process_payment(total, order_items):
    txn_id = str(uuid.uuid4())

    print(f"\nTransaction ID: {txn_id}")

    generate_qr(total)

    print("\nScan the QR code to pay.")

    while True:
        status = input("Payment done? (yes/no): ").lower()

        if status == "yes":
            print("Payment confirmed ✅")
            order = {
                    "items": order_items,
                    "total": total
                }

            send_whatsapp(order)

            # Save order
            with open(ORDER_FILE, "a" ,encoding="utf-8") as f:
                f.write(f"{txn_id} | {order_items} | Total: ₹{total} | PAID\n")

            return True

        elif status == "no":
            print("Payment not completed ❌")
            return False

        else:
            print("Invalid input")
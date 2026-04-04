import webbrowser
import os
import urllib.parse


from dotenv import load_dotenv

load_dotenv()
def send_whatsapp(order):
    
# Step 1: Create message text
    message = "🧾 New Order\n\n"

    for item in order["items"]:
        message += f"{item}\n"

    message += f"\nTotal: ₹{order['total']}"

    # Step 2: Encode message for URL
    encoded_message = urllib.parse.quote(message)

    # Step 3: Owner phone number (with country code)
    phone_number = os.getenv("OWNER_PHONE")  # replace with your number

    # Step 4: Create WhatsApp URL
    url = f"https://wa.me/{phone_number}?text={encoded_message}"

    # Step 5: Open WhatsApp Web
    webbrowser.open(url)
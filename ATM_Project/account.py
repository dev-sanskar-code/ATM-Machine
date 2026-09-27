import hashlib
import random
import sqlite3

from database import get_connection


def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


def generate_card_id():
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        card_id = "VCB" + str(random.randint(100000, 999999))
        cursor.execute("SELECT id FROM accounts WHERE card_id = ?", (card_id,))
        existing = cursor.fetchone()
        if not existing:
            break

    conn.close()
    return card_id


def create_account():
    print("\n--- Create Account ---")

    name = input("Enter your full name: ").strip()
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your full name: ").strip()

    phone = input("Enter your phone number: ").strip()
    while not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Enter a 10-digit number.")
        phone = input("Enter your phone number: ").strip()

    pin = input("Set a 4-digit PIN: ").strip()
    while not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN. Enter a 4-digit number.")
        pin = input("Set a 4-digit PIN: ").strip()

    card_id = generate_card_id()
    pin_hash = hash_pin(pin)

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO accounts (name, phone, card_id, pin_hash, balance) "
            "VALUES (?, ?, ?, ?, ?)",
            (name, phone, card_id, pin_hash, 0)
        )
        conn.commit()
        print("\nAccount created successfully!")
        print("Your Credit Card ID is:", card_id)
        print("Please note it down. You will need it to login.")
    except sqlite3.Error as e:
        print("Database error while creating account:", e)
    finally:
        conn.close()


def login():
    print("\n--- Login ---")
    card_id = input("Enter your Credit Card ID: ").strip()
    pin = input("Enter your PIN: ").strip()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pin_hash FROM accounts WHERE card_id = ?", (card_id,))
    result = cursor.fetchone()
    conn.close()

    if result is None:
        print("Card ID not found.")
        return None

    stored_hash = result[0]
    entered_hash = hash_pin(pin)

    if entered_hash == stored_hash:
        print("Login successful!")
        return card_id
    else:
        print("Incorrect PIN.")
        return None

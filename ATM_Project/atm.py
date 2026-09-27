import sqlite3
from datetime import datetime

from database import get_connection


def get_balance(card_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE card_id = ?", (card_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0]


def check_balance(card_id):
    balance = get_balance(card_id)
    print(f"\nYour current balance is: Rs.{balance}")


def record_transaction(card_id, t_type, amount, balance):
    conn = get_connection()
    cursor = conn.cursor()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO transactions (card_id, type, amount, balance, date) "
        "VALUES (?, ?, ?, ?, ?)",
        (card_id, t_type, amount, balance, date_now)
    )
    conn.commit()
    conn.close()


def deposit(card_id):
    try:
        amount = float(input("\nEnter amount to deposit: Rs."))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be positive.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        new_balance = get_balance(card_id) + amount
        cursor.execute(
            "UPDATE accounts SET balance = ? WHERE card_id = ?",
            (new_balance, card_id)
        )
        conn.commit()
        record_transaction(card_id, "Deposit", amount, new_balance)
        print(f"Rs.{amount} deposited successfully.")
        print(f"New balance: Rs.{new_balance}")
    except sqlite3.Error as e:
        print("Database error during deposit:", e)
    finally:
        conn.close()


def withdraw(card_id):
    try:
        amount = float(input("\nEnter amount to withdraw: Rs."))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be positive.")
        return

    current_balance = get_balance(card_id)

    if amount > current_balance:
        print("Insufficient balance.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        new_balance = current_balance - amount
        cursor.execute(
            "UPDATE accounts SET balance = ? WHERE card_id = ?",
            (new_balance, card_id)
        )
        conn.commit()
        record_transaction(card_id, "Withdraw", amount, new_balance)
        print(f"Rs.{amount} withdrawn successfully.")
        print(f"New balance: Rs.{new_balance}")
    except sqlite3.Error as e:
        print("Database error during withdrawal:", e)
    finally:
        conn.close()


def mini_statement(card_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT type, amount, balance, date FROM transactions "
        "WHERE card_id = ? ORDER BY id DESC LIMIT 5",
        (card_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Mini Statement (Last 5 Transactions) ---")
    if not rows:
        print("No transactions yet.")
        return

    for row in rows:
        t_type, amount, balance, date = row
        print(f"{date} | {t_type:<8} | Rs.{amount:<10} | Balance: Rs.{balance}")


def atm_menu(card_id):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            check_balance(card_id)
        elif choice == "2":
            deposit(card_id)
        elif choice == "3":
            withdraw(card_id)
        elif choice == "4":
            mini_statement(card_id)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

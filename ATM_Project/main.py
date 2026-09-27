from database import create_tables
from account import create_account, login
from atm import atm_menu

BANK_NAME = "The National Central Vellore Institute of Technology and Cooperative Bank Private Limited, Bhopal"


def main():
    create_tables()

    print("=" * 60)
    print(BANK_NAME)
    print("=" * 60)

    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Login / ATM")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            card_id = login()
            if card_id:
                atm_menu(card_id)
        elif choice == "3":
            print("Thank you for using our bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

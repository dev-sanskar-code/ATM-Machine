# ATM Machine / Banking System

**Bank Name:** The National Central Vellore Institute of Technology and Cooperative Bank Private Limited, Bhopal

## About the Project

This is a simple command-line (CLI) based ATM / Banking System built in Python for a first-year college project. It allows users to create an account, log in using a Credit Card ID and PIN, and perform basic banking operations such as checking balance, depositing money, withdrawing money, and viewing a mini statement. All data is stored using SQLite.

## Features

- Create account
- Automatic Credit Card ID generation
- PIN hashing (SHA-256)
- Login
- Check balance
- Deposit
- Withdraw
- Mini statement
- SQLite database
- CLI interface

## Technologies Used

- Python
- SQLite
- hashlib

## Project Structure

```
ATM_Project/
│
├── main.py            # Entry point, shows main menu, connects everything
├── database.py         # Creates the database and tables, gives DB connection
├── account.py          # Account creation, Credit Card ID generation, PIN hashing, login
├── atm.py               # ATM menu: balance, deposit, withdraw, mini statement
├── README.md
├── statement.md
└── requirements.txt
```

- **main.py** – Starts the program, shows the main menu (Create Account / Login / Exit), and calls functions from the other modules.
- **database.py** – Connects to the SQLite database (`atm.db`) and creates the `accounts` and `transactions` tables if they don't already exist.
- **account.py** – Handles creating a new account, generating a unique Credit Card ID, hashing the PIN, and verifying login credentials.
- **atm.py** – Handles all ATM operations after login: checking balance, depositing, withdrawing, and showing the mini statement.

## How to Run

Make sure you have Python 3.10+ installed. Then run:

```
python main.py
```

The database file `atm.db` will be created automatically in the same folder the first time you run the program.

## Database

The project uses two tables in SQLite:

- **accounts** – stores `id`, `name`, `phone`, `card_id`, `pin_hash`, and `balance` for each user.
- **transactions** – stores `id`, `card_id`, `type` (Deposit/Withdraw), `amount`, `balance` (after the transaction), and `date` for every transaction made.

## Security

The user's PIN is never stored as plain text. When an account is created, the PIN is passed through Python's `hashlib.sha256()` function, and only the resulting hash is stored in the database. During login, the entered PIN is hashed again and compared to the stored hash. SHA-256 is a one-way hashing function (not reversible encryption), so this project only demonstrates a basic, educational approach to password/PIN safety — it is not meant for real-world banking security.

## Future Improvements

- Add PIN change / forgot PIN option
- Add a transaction limit per day
- Add an admin panel to view all accounts
- Export mini statement to a text/PDF file
- Add multi-currency support

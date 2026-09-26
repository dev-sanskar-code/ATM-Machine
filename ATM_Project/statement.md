# Project Statement

## Problem Statement

The National Central Vellore Institute of Technology and Cooperative Bank Private Limited, Bhopal requires a simple computerized ATM system that allows its customers to create an account and perform basic banking operations such as checking balance, depositing money, and withdrawing money, without needing a physical bank visit for every small transaction.

## Objective

To design and develop a simple, terminal-based ATM Machine simulation using Python and SQLite that demonstrates the core concepts of account management, authentication, and transaction handling.

## Proposed Solution

A Python CLI application is proposed that lets a user create an account with a name, phone number, and self-chosen PIN. On account creation, the system automatically generates a unique Credit Card ID. The user can then log in using this Credit Card ID and PIN to access an ATM menu where they can check their balance, deposit money, withdraw money, and view a mini statement of their recent transactions. All account and transaction data is stored persistently using an SQLite database, and PINs are stored securely using SHA-256 hashing.

## Main Features

- Account creation with auto-generated Credit Card ID
- Secure PIN storage using SHA-256 hashing
- Login authentication using Credit Card ID and PIN
- Balance inquiry
- Deposit and withdrawal with input validation
- Mini statement showing recent transactions
- Persistent storage using SQLite

## Technologies Used

- Python 3
- SQLite (via Python's built-in `sqlite3` module)
- `hashlib` for PIN hashing
- `datetime` for recording transaction timestamps

## Expected Outcome

A working command-line ATM system where a user can create an account, receive a unique Credit Card ID, log in securely, and perform deposit, withdrawal, and balance-check operations, with all data correctly saved and retrieved from an SQLite database even after the program is closed and reopened.

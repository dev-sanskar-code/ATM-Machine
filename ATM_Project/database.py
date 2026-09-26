"""
database.py
Handles the SQLite database connection and table creation.
"""

import sqlite3

DB_NAME = "atm.db"


def get_connection():
    """Return a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def create_tables():
    """Create the accounts and transactions tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            card_id TEXT UNIQUE NOT NULL,
            pin_hash TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id TEXT NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

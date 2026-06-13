# database.py
# This file handles everything related to the SQLite database.
# We keep it separate from app.py to keep the code clean and organized.

import sqlite3

# The name of our database file.
# SQLite will create this file automatically when the app runs.
DATABASE = "urls.db"


def get_db_connection():
    """
    Opens a connection to the SQLite database.
    Returns the connection object so we can run queries.
    """
    conn = sqlite3.connect(DATABASE)

    # This makes rows behave like dictionaries.
    # So instead of row[0], we can write row["short_code"] — much clearer.
    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    """
    Creates the 'urls' table if it doesn't already exist.
    This function is called once when the app starts.
    """
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code   TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL,
            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()   # Save the changes
    conn.close()    # Always close the connection when done


def save_url(short_code, original_url):
    """
    Saves a new short_code + original_url pair into the database.
    Called after we generate a short code for the user's URL.
    """
    conn = get_db_connection()

    conn.execute(
        "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
        (short_code, original_url)
    )

    conn.commit()
    conn.close()


def find_url(short_code):
    """
    Looks up the original URL for a given short code.
    Returns the row (with original_url) if found, or None if not found.
    Called when a user visits a short link.
    """
    conn = get_db_connection()

    row = conn.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    ).fetchone()  # fetchone() returns the first match, or None

    conn.close()

    return row
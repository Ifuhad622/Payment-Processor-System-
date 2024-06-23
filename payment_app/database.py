import sqlite3

def initialize_database():
    conn = sqlite3.connect('payments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    date TEXT,
                    time TEXT,
                    year INTEGER,
                    amount_due REAL,
                    payment_amount REAL,
                    remaining_balance REAL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )''')
    conn.commit()
    conn.close()

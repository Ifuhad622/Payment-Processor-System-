import datetime
import sqlite3

class PaymentProcessor:
    def __init__(self):
        self.conn = sqlite3.connect('payments.db')
        self.c = self.conn.cursor()
    
    def add_user(self, name):
        self.c.execute('INSERT INTO users (name) VALUES (?)', (name,))
        self.conn.commit()
        print(f"User '{name}' added successfully.")
    
    def get_user_id(self, name):
        self.c.execute('SELECT id FROM users WHERE name = ?', (name,))
        user = self.c.fetchone()
        return user[0] if user else None
    
    def make_payment(self, user_name, amount_due, payment_amount):
        user_id = self.get_user_id(user_name)
        if not user_id:
            print(f"User '{user_name}' not found.")
            return
        
        now = datetime.datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')
        year = now.year
        
        self.c.execute('SELECT SUM(remaining_balance) FROM payments WHERE user_id = ?', (user_id,))
        previous_balance = self.c.fetchone()[0] or 0.0
        
        total_due = amount_due + previous_balance
        if payment_amount >= total_due:
            change = payment_amount - total_due
            remaining_balance = 0.0
            print(f"Payment successful! Change: ${change:.2f}")
        else:
            remaining_balance = total_due - payment_amount
            print(f"Payment successful! Remaining Balance: ${remaining_balance:.2f}")
        
        self.c.execute('''INSERT INTO payments (user_id, date, time, year, amount_due, payment_amount, remaining_balance)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (user_id, date_str, time_str, year, amount_due, payment_amount, remaining_balance))
        self.conn.commit()
        
        print(f"Date: {date_str}")
        print(f"Time: {time_str}")
        print(f"Year: {year}")
        print(f"Total Amount Due: ${total_due:.2f}")
        print(f"Payment Amount: ${payment_amount:.2f}")
        print(f"Invoice: \n\tAmount Due: ${amount_due:.2f}\n\tPayment: ${payment_amount:.2f}\n\tRemaining Balance: ${remaining_balance:.2f}")
        print("="*50)
    
    def close(self):
        self.conn.close()

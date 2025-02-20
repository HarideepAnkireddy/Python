from database import load_users, save_users

def check_balance(username):
    users = load_users()
    print(f"Your balance: 💰 ${users[username]['balance']}")

def deposit_money(username):
    users = load_users()
    amount = float(input("Enter amount to deposit: ").strip())

    if amount > 0:
        users[username]['balance'] += amount
        save_users(users)
        print(f"✅ Deposited ${amount}. New balance: ${users[username]['balance']}")
    else:
        print("Error: Amount must be greater than zero.")

def withdraw_money(username):
    users = load_users()
    amount = float(input("Enter amount to withdraw: ").strip())

    if 0 < amount <= users[username]['balance']:
        users[username]['balance'] -= amount
        save_users(users)
        print(f"✅ Withdrawn ${amount}. Remaining balance: ${users[username]['balance']}")
    else:
        print("Error: Insufficient balance or invalid amount.")

from database import load_users, save_users
from utils import validate_amount

def check_balance(username):
    """Display wallet balance."""
    users = load_users()
    print(f"Current Balance: ${users[username]['balance']}")

def deposit_money(username):
    """Add funds to the wallet."""
    amount = input("Enter amount to deposit: ").strip()
    if not validate_amount(amount):
        print("Error: Invalid amount!")
        return

    users = load_users()
    users[username]['balance'] += float(amount)
    save_users(users)
    print(f"Balance Updated! New Balance: ${users[username]['balance']}")

def withdraw_money(username):
    """Deduct money from wallet."""
    amount = input("Enter amount to withdraw: ").strip()
    if not validate_amount(amount):
        print("Error: Invalid amount!")
        return

    users = load_users()
    if users[username]['balance'] >= float(amount):
        users[username]['balance'] -= float(amount)
        save_users(users)
        print(f"Transaction Successful! New Balance: ${users[username]['balance']}")
    else:
        print("Error: Insufficient Balance!")

from database import load_users, save_users
from utils import validate_amount
from datetime import datetime  # Import datetime for timestamps

def check_balance(username):
    users = load_users()
    balance = users[username]['balance']

    print(f"Your balance: 💰 ${balance}")

    if balance < 100:
        print("⚠️ Low balance!")
    elif balance > 500:
        print("You are very rich")

def deposit_money(username):
    """Add funds to the wallet and record transaction."""
    amount = input("Enter amount to deposit: ").strip()
    if not validate_amount(amount):
        print("Error: Invalid amount!")
        return

    users = load_users()
    users[username]['balance'] += float(amount)

    # Ensure transactions list exists
    if "transactions" not in users[username] or users[username]["transactions"] is None:
        users[username]["transactions"] = []

    # Save transaction
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "Deposit",
        "amount": float(amount),
        "balance": users[username]['balance']
    }
    users[username]["transactions"].append(transaction)

    save_users(users)
    print(f"✅ Balance Updated! New Balance: ${users[username]['balance']}")

def withdraw_money(username):
    """Deduct money from wallet and record transaction."""
    amount = input("Enter amount to withdraw: ").strip()
    if not validate_amount(amount):
        print("Error: Invalid amount!")
        return

    users = load_users()
    if users[username]['balance'] >= float(amount):
        users[username]['balance'] -= float(amount)

        # Ensure transactions list exists
        if "transactions" not in users[username] or users[username]["transactions"] is None:
            users[username]["transactions"] = []

        # Save transaction
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "Withdrawal",
            "amount": float(amount),
            "balance": users[username]['balance']
        }
        users[username]["transactions"].append(transaction)

        save_users(users)
        print(f"✅ Transaction Successful! New Balance: ${users[username]['balance']}")
    else:
        print("❌ Error: Insufficient Balance!")

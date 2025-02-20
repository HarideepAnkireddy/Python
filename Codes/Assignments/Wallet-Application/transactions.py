from database import load_users

def view_transactions(username):
    users = load_users()
    transactions = users[username].get('transactions', [])

    if transactions:
        print("\n📜 Transaction History:")
        for txn in transactions:
            print(f"{txn['date']} - {txn['type']} ${txn['amount']}")
    else:
        print("No transactions found.")

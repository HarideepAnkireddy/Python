from database import load_users

def view_transactions(username):
    """Display transaction history."""
    users = load_users()
    print("Date        | Type    | Amount  | Balance")
    print("--------------------------------------")
    for txn in users[username].get("transactions", []):
        print(f"{txn['date']} | {txn['type']} | ${txn['amount']} | ${txn['balance']}")

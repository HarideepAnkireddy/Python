import json
import os

USER_DB = "users.json"
TRANSACTION_DB = "transactions.json"

# Initialize JSON files if they don’t exist
def initialize_files():
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w") as file:
            json.dump({}, file)

    if not os.path.exists(TRANSACTION_DB):
        with open(TRANSACTION_DB, "w") as file:
            json.dump({}, file)

# Load user data
def load_users():
    with open(USER_DB, "r") as file:
        return json.load(file)

# Save user data
def save_users(data):
    with open(USER_DB, "w") as file:
        json.dump(data, file, indent=4)

# Load transaction history
def load_transactions():
    with open(TRANSACTION_DB, "r") as file:
        return json.load(file)

# Save transaction history
def save_transactions(data):
    with open(TRANSACTION_DB, "w") as file:
        json.dump(data, file, indent=4)

initialize_files()

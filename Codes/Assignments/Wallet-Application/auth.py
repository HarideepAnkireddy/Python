from database import load_users, save_users
from utils import validate_username, validate_password
import getpass

def register_user():
    """Register a new user with an initial balance."""
    users = load_users()
    username = input("Enter username: ").strip()

    if not validate_username(username):
        print("Error: Username cannot be empty!")
        return

    if username in users:
        print("Error: Username already exists!")
        return

    password = getpass.getpass("Enter your password (at least 5 characters): ").strip()
    if not validate_password(password):
        print("Error: Password must be at least 5 characters long.")
        return

    users[username] = {"password": password, "balance": 0, "profile": {}, "transactions": []}
    save_users(users)
    print("✅ User Registered Successfully!")

def login_user():
    """Authenticate a user."""
    users = load_users()
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    if username in users and users[username]["password"] == password:
        print("✅ Login successful!")
        return username
    else:
        print("Error: Invalid username or password.")
        return None

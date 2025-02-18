import os
import hashlib

# File to store user data
USER_FILE = "users.txt"

def hash_password(password):
    """Hashes the password using SHA-256 for security."""
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    """Checks if the username already exists in the file."""
    if not os.path.exists(USER_FILE):
        return False  # File doesn't exist yet, so no users are registered

    with open(USER_FILE, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(",")
            if stored_username == username:
                return True  # Username found
    return False  # Username not found

def register_user():
    """Registers a new user and stores their credentials securely."""
    try:
        username = input("Enter a username: ").strip()
        if not username:
            raise ValueError("Username cannot be empty!")

        if user_exists(username):
            print("Error: Username already exists! Choose a different one.")
            return

        password = input("Enter a password: ").strip()
        if not password:
            raise ValueError("Password cannot be empty!")

        hashed_password = hash_password(password)

        # Store username and hashed password in the file
        with open(USER_FILE, "a") as file:
            file.write(f"{username},{hashed_password}\n")

        print("User registered successfully!")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Run the registration process
if __name__ == "__main__":
    register_user()

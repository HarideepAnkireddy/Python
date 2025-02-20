from database import load_users, save_users

def update_profile(username):
    """Update user profile details."""
    users = load_users()
    email = input("Enter new email: ").strip()
    phone = input("Enter new phone number: ").strip()

    users[username]["profile"] = {"email": email, "phone": phone}
    save_users(users)
    print("Profile Updated Successfully!")

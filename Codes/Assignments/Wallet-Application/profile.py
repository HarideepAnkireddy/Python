from database import load_users, save_users

def update_profile(username):
    users = load_users()
    name = input("Enter your full name: ").strip()
    email = input("Enter your email: ").strip()

    users[username]['profile'] = {"name": name, "email": email}
    save_users(users)
    print("✅ Profile updated successfully!")

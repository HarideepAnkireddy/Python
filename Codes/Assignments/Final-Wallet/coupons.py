COUPONS = {
    "SAVE10": 0.10,
    "BONUS20": 0.20
}

from database import load_users, save_users

def apply_coupon(username):
    """Apply a coupon code."""
    code = input("Enter coupon code: ").strip().upper()

    if code in COUPONS:
        users = load_users()
        bonus = users[username]["balance"] * COUPONS[code]
        users[username]["balance"] += bonus
        save_users(users)
        print(f"Coupon Applied! You received a {COUPONS[code] * 100}% bonus.")
        print(f"New Balance: ${users[username]['balance']}")
    else:
        print("Error: Invalid Coupon Code!")

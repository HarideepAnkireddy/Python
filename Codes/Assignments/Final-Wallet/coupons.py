COUPONS = {
    "DASARA": 0.10,  # 10% bonus
    "DIWALI": 0.25   # 25% bonus
}

from database import load_users, save_users

def apply_coupon(username):
    """Apply a coupon code."""
    code = input("Enter coupon code (DASARA/DIWALI): ").strip().upper()

    if code in COUPONS:
        users = load_users()
        bonus = users[username]["balance"] * COUPONS[code]
        users[username]["balance"] += bonus
        save_users(users)
        print(f"✅ Coupon '{code}' applied! You received a {COUPONS[code] * 100}% bonus.")
        print(f"New Balance: ${users[username]['balance']:.2f}")
    else:
        print("❌ Error: Invalid Coupon Code!")

from database import load_users, save_users

COUPONS = {"SAVE10": 10, "SAVE20": 20}

def apply_coupon(username):
    users = load_users()
    coupon_code = input("Enter coupon code: ").strip().upper()

    if coupon_code in COUPONS:
        discount = COUPONS[coupon_code]
        users[username]['balance'] += discount
        save_users(users)
        print(f"✅ Coupon applied! ${discount} added to your balance.")
    else:
        print("Error: Invalid coupon code.")

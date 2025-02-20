from auth import register_user, login_user
from wallet import check_balance, deposit_money, withdraw_money
from coupons import apply_coupon
from transactions import view_transactions
from profile import update_profile

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def display_banner():
    print("=" * 40)
    print("      🏦 Welcome to Your E-Wallet! 💰     ")
    print("=" * 40)

display_banner()


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user:
                while True:
                    print(
                        "\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Apply Coupon\n5. Transaction History\n6. Update Profile\n7. Logout")
                    option = input("Enter choice: ").strip()

                    if option == "1":
                        check_balance(user)
                    elif option == "2":
                        deposit_money(user)
                    elif option == "3":
                        withdraw_money(user)
                    elif option == "4":
                        apply_coupon(user)
                    elif option == "5":
                        view_transactions(user)
                    elif option == "6":
                        update_profile(user)
                    elif option == "7":
                        break
        elif choice == "3":
            break


if __name__ == "__main__":
    main()



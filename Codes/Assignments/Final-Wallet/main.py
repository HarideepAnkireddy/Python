import time
import sys
from auth import register_user, login_user
from wallet import check_balance, deposit_money, withdraw_money
from coupons import apply_coupon
from transactions import view_transactions
from profile import update_profile


def new_logout():
    """Displays a smooth logout animation."""
    print("\nLogging out", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n✅ Logged out successfully! See you soon. 👋")


def main():
    while True:
        print("\n🔹 1. Register\n🔹 2. Login\n🔹 3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user:
                while True:
                    print(
                        "\n🔹 1. Check Balance\n🔹 2. Deposit\n🔹 3. Withdraw\n🔹 4. Apply Coupon"
                        "\n🔹 5. Transaction History\n🔹 6. Update Profile\n🔹 7. Logout"
                    )
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
                        new_logout()
                        break
        elif choice == "3":
            print("\n👋 Exiting... Have a great day!")
            break


if __name__ == "__main__":
    main()

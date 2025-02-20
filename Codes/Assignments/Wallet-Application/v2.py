import json
import datetime


class Wallet:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []
        self.profile = {"email": "", "phone": ""}

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            print(f"Balance Updated! New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient Balance!")
        elif amount > 0:
            self.balance -= amount
            self.add_transaction("Withdraw", -amount)
            print(f"Transaction Successful! New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount!")

    def apply_coupon(self, code):
        coupons = {"SAVE10": 0.10, "BONUS20": 0.20}
        if code in coupons:
            bonus = self.balance * coupons[code]
            self.balance += bonus
            self.add_transaction("Coupon", bonus)
            print(f"Coupon Applied! You received a {coupons[code] * 100}% bonus.")
            print(f"New Balance: ${self.balance}")
        else:
            print("Invalid coupon code!")

    def add_transaction(self, trans_type, amount):
        transaction = {
            "date": str(datetime.datetime.now().date()),
            "type": trans_type,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(transaction)

    def view_transactions(self):
        print("Date         | Type     | Amount | Balance")
        print("------------------------------------------")
        for txn in self.transactions:
            print(f"{txn['date']} | {txn['type']} | ${txn['amount']} | ${txn['balance']}")

    def update_profile(self, email, phone):
        self.profile["email"] = email
        self.profile["phone"] = phone
        print("Profile Updated Successfully!")


class WalletApp:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            print("Username already exists!")
            return
        self.users[username] = Wallet(username, password, 0)
        print("User Registered Successfully!")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("Login Successful!")
            return self.users[username]
        else:
            print("Invalid credentials!")
            return None


if __name__ == "__main__":
    app = WalletApp()

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            app.register(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = app.login(username, password)

            if user:
                while True:
                    print(
                        "\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Apply Coupon\n5. View Transactions\n6. Update Profile\n7. Logout")
                    option = input("Enter option: ")

                    if option == "1":
                        print(f"Current Balance: ${user.balance}")
                    elif option == "2":
                        amt = float(input("Enter amount to deposit: "))
                        user.deposit(amt)
                    elif option == "3":
                        amt = float(input("Enter amount to withdraw: "))
                        user.withdraw(amt)
                    elif option == "4":
                        code = input("Enter coupon code: ")
                        user.apply_coupon(code)
                    elif option == "5":
                        user.view_transactions()
                    elif option == "6":
                        email = input("Enter new email: ")
                        phone = input("Enter new phone: ")
                        user.update_profile(email, phone)
                    elif option == "7":
                        print("Logged out!")
                        break
                    else:
                        print("Invalid option!")

        elif choice == "3":
            print("Exiting application!")
            break
        else:
            print("Invalid choice!")

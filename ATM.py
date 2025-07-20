import datetime

class ATM:
    def __init__(self, initial_balance, pin):
        self.balance = initial_balance
        self.pin = pin
        self.transactions = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
        self.log_transaction("Balance Inquiry")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}")
            self.log_transaction(f"Deposit: ${amount:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}. Your new balance is ${self.balance:.2f}")
                self.log_transaction(f"Withdrawal: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.pin = new_pin
            print("PIN successfully changed.")
            self.log_transaction("PIN Change")
        else:
            print("Incorrect current PIN.")

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def log_transaction(self, transaction):
        self.transactions.append(f"{datetime.datetime.now()}: {transaction}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)

def main():
    atm = ATM(initial_balance=1000.0, pin="1234")

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            atm.show_transactions()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

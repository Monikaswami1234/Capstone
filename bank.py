class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.name}'s account.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.name}'s account.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def display_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


def main():
    # Get user input for account details
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))

    # Create bank account object
    account = BankAccount(name, initial_balance)

    # Perform transactions
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Display Details\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display_details()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

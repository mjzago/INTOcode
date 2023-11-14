class BankAccount:
    def _init_(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter an amount greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal cannot be processed.")
        else:
            print("Invalid withdrawal amount. Please enter an amount greater than zero.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


if _name_ == "_main_":
    account = BankAccount()

    while True:
        print("\n--- Bank Account Simulator ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            deposit_amount = float(input("Enter the amount to deposit: "))
            account.deposit(deposit_amount)
        elif choice == '2':
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(withdraw_amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting the bank account simulator. Thank you!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")
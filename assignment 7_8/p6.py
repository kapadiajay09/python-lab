class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print(f"Account {self.account_number} - Balance: {self.balance}")


account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, initial_balance)

while True:
    print("\nBank Account Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '3':
        account.display()
    elif choice == '4':
        print("Exiting Bank Account System.")
        break
    else:
        print("Invalid choice. Please try again.")

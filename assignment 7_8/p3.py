class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
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

    def display_balance(self):
        print(f"Account {self.account_number} - Owner: {self.owner}, Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, owner, initial_deposit)
            print("Account created successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


bank = Bank()
while True:
    print("\nBank System:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        acc_num = input("Enter account number: ")
        owner = input("Enter account owner name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        bank.create_account(acc_num, owner, initial_deposit)
    elif choice == '2':
        acc_num = input("Enter account number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("Account not found.")
    elif choice == '3':
        acc_num = input("Enter account number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        else:
            print("Account not found.")
    elif choice == '4':
        acc_num = input("Enter account number: ")
        account = bank.get_account(acc_num)
        if account:
            account.display_balance()
        else:
            print("Account not found.")
    elif choice == '5':
        print("Exiting Bank System.")
        break
    else:
        print("Invalid choice. Please try again.")

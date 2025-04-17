class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
       
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
       
        return password == self.get_password()



pm = Password_manager()

while True:
    print("\nMenu:")
    print("1.Set a new password")
    print("2.Get the current password")
    print("3.Verify")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        new_pass = input("Enter a new password: ")
        if pm.set_password(new_pass):
            print("Password updated successfully")
        else:
            print("choose a different password")
    
    elif choice == "2":
        current_pass = pm.get_password()
        if current_pass:
            print(f"Your current password is: {current_pass}")
        else:
            print("No password set.")

    elif choice == "3":
        check_pass = input("Enter password to verify: ")
        if pm.is_correct(check_pass):
            print("Correct password!")
        else:
            print("Incorrect password.")

    elif choice == "4":
        print("Exiting Password Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

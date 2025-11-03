import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to MyBank!")

bankAccounts = []

passwords = []

register = input("Do you want to register a new bank account? (yes/no): \n").strip().lower()
clear_screen()
if register == "yes":
    name = input("Enter your name:\n")
    password = input("Create a password for your account:\n")

    bankAccounts.append(name)
    passwords.append(password)

    initial_deposit = float(input("Enter initial deposit amount:\n"))
    clear_screen()
    print(f"Account created for {name} with an initial deposit of Ugx shs.{initial_deposit}")
    print("You can now log in to your account.")

login = input("Do you want to log in to your account? (yes/no): \n").strip().lower()
clear_screen()

if login == "yes":
    name = input("Enter your name:\n")
    password = input("Enter your password:\n")
    clear_screen()

    if name in bankAccounts:
        index = bankAccounts.index(name)
        if passwords[index] == password:
            print(f"Login successful. Welcome back, {name}!")
        else:
            clear_screen()
            print("Incorrect password.")
            exit()
    else:
        print("Account not found.")
        exit()

else:
    
    print("Thank you for using MyBank. Goodbye!")

logged_in = True

while logged_in:
    print("\nSelect an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Logout")

    choice = input("Enter your choice (1-4): \n").strip()
    clear_screen()

    if choice == "1":
        deposit_amount = float(input("Enter amount to deposit:\n"))
        initial_deposit += deposit_amount
        print(f"Deposited Ugx shs.{deposit_amount}. New balance is Ugx shs.{initial_deposit}")

    elif choice == "2":
        withdraw_amount = float(input("Enter amount to withdraw:\n"))
        if withdraw_amount <= initial_deposit:
            initial_deposit -= withdraw_amount
            print(f"You have withdrawn Ugx shs.{withdraw_amount}. New balance is Ugx shs.{initial_deposit}")
        else:
            clear_screen()
            print("Insufficient funds.")

    elif choice == "3":
            clear_screen()
            print(f"Your current balance is Ugx shs.{initial_deposit}")

    elif choice == "4":
        clear_screen
        print("Logging out...")
        logged_in = False

    else:
        clear_screen()
        print("Invalid choice. Please try again.")

else:
    clear_screen()
    print("Thank you for using MyBank. Goodbye!")
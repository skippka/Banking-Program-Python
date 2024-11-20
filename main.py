from getpass import getpass
from colorama import Fore, Back, Style
from colorama import init
import time

class PREFIX:
    CORRECT_PREFIX = Fore.GREEN + "[i] - " + Style.RESET_ALL
    INFO_PREFIX = Fore.BLUE + "[i] - " + Style.RESET_ALL
    WARN_PREFIX = Fore.YELLOW + "[i] - " + Style.RESET_ALL
    ERROR_PREFIX = Fore.RED + "[i] - " + Style.RESET_ALL



def show_balance():
    print(f"{PREFIX.CORRECT_PREFIX} You have ${balance:.2f}" + Style.RESET_ALL)

def deposit():
    amount = float(input( PREFIX.INFO_PREFIX + "Enter the amount to be deposited: "))

    if amount < 0:
        print(f"{PREFIX.WARN_PREFIX} Thats not a valid amount! ")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input(PREFIX.INFO_PREFIX + "Enter the amount to be withdrawn: "))

    if amount > balance:
        print(f"{PREFIX.WARN_PREFIX} Insufficient funds! ")
        return 0
    elif amount < 0:
        print(f"{PREFIX.WARN_PREFIX} Amount must be greater than 0")
    else:
        return amount

balance = 0


init()

password = getpass("Password: ")

correct_password = "qwerty"

if password == correct_password:
    print("Login...")
    time.sleep(2)

    print(PREFIX.CORRECT_PREFIX + "Login Successful!")
    is_running = True
else:
    print(PREFIX.WARN_PREFIX + "Unconfirmed password!")
    is_running = False


while is_running:
    print("Banking Program Python")
    print("")
    print("1 - Show Balance")
    print("")
    print("2 - Deposit")
    print("")
    print("3 - Withdraw")
    print("")
    print("4 - Exit")
    print("")
    choice = input("Выберите свой раздел (1-4):")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print(PREFIX.ERROR_PREFIX + "That is not a valid choise")

print(PREFIX.CORRECT_PREFIX + "Thank you for using!")



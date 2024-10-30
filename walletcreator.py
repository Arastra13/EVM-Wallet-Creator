from eth_account import Account
import os
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# ASCII art in green
def display_banner():
    banner = """
     █████  ██████   █████  ███████ ████████ ██████   █████  
    ██   ██ ██   ██ ██   ██ ██         ██    ██   ██ ██   ██ 
    ███████ ██████  ███████ ███████    ██    ██████  ███████ 
    ██   ██ ██   ██ ██   ██      ██    ██    ██   ██ ██   ██ 
    ██   ██ ██   ██ ██   ██ ███████    ██    ██   ██ ██   ██ 
    """
    print(Fore.GREEN + banner)

def create_wallets(num_wallets):
    wallets = []
    for _ in range(num_wallets):
        acct = Account.create()
        wallets.append((acct.key.hex(), acct.address))  # Collect both private key and address
    return wallets

def save_to_files(wallets, private_key_filename='pvkey.txt', address_filename='address.txt'):
    # Open the files in append mode to continue writing without removing previous data
    with open(private_key_filename, 'a') as pvkey_file, open(address_filename, 'a') as address_file:
        for private_key, address in wallets:
            pvkey_file.write(f"{private_key}\n")   # Save each private key with single newline
            address_file.write(f"{address}\n")     # Save each address with single newline

def main():
    display_banner()  # Display the ASCII art at the start
    try:
        num_wallets = int(input("How many wallets do you want to create? "))
        if num_wallets <= 0:
            print("Please enter a positive integer.")
            return
        wallets = create_wallets(num_wallets)
        save_to_files(wallets)
        print(f"{num_wallets} wallets created. Private keys saved to pvkey.txt and addresses saved to address.txt.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

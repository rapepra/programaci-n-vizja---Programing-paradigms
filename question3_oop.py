# Question 3: Smart ATM Transaction System - Object-Oriented Programming (OOP)
# Approach:
# Model bank accounts using a BankAccount class with deposit, withdraw, and is_vip methods.
# For each transaction, find or create the account and call the appropriate method.

transactions = [
    ("Alice", "deposit", 5000),
    ("Bob", "withdraw", 2000),
    ("Alice", "withdraw", 1500),
    ("Charlie", "deposit", 3000),
    ("Bob", "deposit", 4000),
    ("Alice", "withdraw", 1000),
]


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def is_vip(self):
        return self.balance > 3000


def process_accounts(tx_list):
    accounts = {}

    for name, action, amount in tx_list:
        if name not in accounts:
            accounts[name] = BankAccount(name)

        if action == "deposit":
            accounts[name].deposit(amount)
        elif action == "withdraw":
            accounts[name].withdraw(amount)

    return accounts


def main():
    # Standard output
    accounts = process_accounts(transactions)
    for name, acc in accounts.items():
        print(f"{name} : {acc.balance}")

    # Bonus task
    print("\nBonus:")
    bonus_transactions = transactions + [("Charlie", "deposit", 2000)]
    bonus_accounts = process_accounts(bonus_transactions)

    for name, acc in bonus_accounts.items():
        if acc.is_vip():
            print(f"{name} : {acc.balance} (VIP)")
        else:
            print(f"{name} : {acc.balance}")


if __name__ == "__main__":
    main()

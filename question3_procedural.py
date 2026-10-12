"""
Assignment 1 - Question 3: Smart ATM Transaction System
Paradigm 1: Procedural Programming

Approach:
In procedural programming, we process transactions step by step using loops,
variables, and conditional statements.
We store customer balances in a dictionary, iterate through each transaction,
and update the balance depending on whether it is a deposit or a withdrawal.
For the bonus, we add Charlie's extra transaction and check if any balance exceeds 3000.
"""

transactions = [
    ("Alice", "deposit", 5000),
    ("Bob", "withdraw", 2000),
    ("Alice", "withdraw", 1500),
    ("Charlie", "deposit", 3000),
    ("Bob", "deposit", 4000),
    ("Alice", "withdraw", 1000),
]


def process_transactions(tx_list):
    balances = {}

    for customer, action, amount in tx_list:
        if customer not in balances:
            balances[customer] = 0

        if action == "deposit":
            balances[customer] += amount
        elif action == "withdraw":
            balances[customer] -= amount

    return balances


def main():
    # Expected output
    balances = process_transactions(transactions)
    for customer, balance in balances.items():
        print(f"{customer} : {balance}")

    # Bonus task
    print("\nBonus:")
    bonus_transactions = transactions + [("Charlie", "deposit", 2000)]
    bonus_balances = process_transactions(bonus_transactions)

    for customer, balance in bonus_balances.items():
        if balance > 3000:
            print(f"{customer} : {balance} (VIP)")
        else:
            print(f"{customer} : {balance}")


if __name__ == "__main__":
    main()

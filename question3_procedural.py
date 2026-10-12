# Question 3: Smart ATM Transaction System - Procedural Programming
# Approach:
# Process transactions step by step using a loop and a dictionary.
# Update balances with if/elif conditions for deposit and withdraw, and check VIP status for the bonus.

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

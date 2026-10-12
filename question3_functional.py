"""
Assignment 1 - Question 3: Smart ATM Transaction System
Paradigm 3: Functional Programming (FP)

Approach:
In Functional Programming, we avoid mutating state variables.
Instead, we use pure functions and higher-order functions like map(), filter(), reduce(), and lambda.
1. We filter transactions for each customer.
2. We map each transaction to its signed amount (+ for deposit, - for withdraw).
3. We reduce the signed amounts to compute the customer's final balance.
4. For the bonus, we filter customers whose balance is above 3000 to identify VIPs.
"""

from functools import reduce

transactions = [
    ("Alice", "deposit", 5000),
    ("Bob", "withdraw", 2000),
    ("Alice", "withdraw", 1500),
    ("Charlie", "deposit", 3000),
    ("Bob", "deposit", 4000),
    ("Alice", "withdraw", 1000),
]


def get_balance(customer, tx_list):
    # Filter transactions belonging to the customer
    customer_tx = filter(lambda tx: tx[0] == customer, tx_list)

    # Map each transaction into a signed value
    signed_amounts = map(
        lambda tx: tx[2] if tx[1] == "deposit" else -tx[2],
        customer_tx
    )

    # Reduce amounts to calculate total balance
    return reduce(lambda acc, val: acc + val, signed_amounts, 0)


def get_all_balances(tx_list):
    # Get distinct customer names
    customers = list(dict.fromkeys(tx[0] for tx in tx_list))

    # Map each customer to (customer, balance)
    balances = map(lambda name: (name, get_balance(name, tx_list)), customers)
    return dict(balances)


def main():
    # Standard output
    balances = get_all_balances(transactions)
    for name, bal in balances.items():
        print(f"{name} : {bal}")

    # Bonus task
    print("\nBonus:")
    bonus_transactions = transactions + [("Charlie", "deposit", 2000)]
    bonus_balances = get_all_balances(bonus_transactions)

    # Use filter and lambda to classify VIPs
    vip_names = set(
        map(
            lambda item: item[0],
            filter(lambda item: item[1] > 3000, bonus_balances.items())
        )
    )

    for name, bal in bonus_balances.items():
        if name in vip_names:
            print(f"{name} : {bal} (VIP)")
        else:
            print(f"{name} : {bal}")


if __name__ == "__main__":
    main()

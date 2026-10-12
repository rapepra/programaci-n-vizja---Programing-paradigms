# Question 3: Four Programming Paradigms - Smart ATM Transaction System
# Approach:
# We solve the ATM transaction problem using 4 different paradigms:
# 1. Procedural: updates balances sequentially in a dictionary with loops and if/elif.
# 2. OOP: uses a BankAccount class with deposit, withdraw, and is_vip methods.
# 3. Functional: uses map, filter, reduce, and lambda without mutating state.
# 4. Logical: defines Facts and deductive Rules to determine balances and VIP status.

from functools import reduce

transactions = [
    ("Alice", "deposit", 5000),
    ("Bob", "withdraw", 2000),
    ("Alice", "withdraw", 1500),
    ("Charlie", "deposit", 3000),
    ("Bob", "deposit", 4000),
    ("Alice", "withdraw", 1000),
]

bonus_transactions = transactions + [("Charlie", "deposit", 2000)]


# 1. Procedural Programming
def run_procedural(tx_list, show_vip=False):
    balances = {}
    for name, action, amount in tx_list:
        if name not in balances:
            balances[name] = 0

        if action == "deposit":
            balances[name] += amount
        elif action == "withdraw":
            balances[name] -= amount

    for name, balance in balances.items():
        vip_tag = " (VIP)" if (show_vip and balance > 3000) else ""
        print(f"{name} : {balance}{vip_tag}")


# 2. Object-Oriented Programming (OOP)
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


def run_oop(tx_list, show_vip=False):
    accounts = {}
    for name, action, amount in tx_list:
        if name not in accounts:
            accounts[name] = BankAccount(name)

        if action == "deposit":
            accounts[name].deposit(amount)
        elif action == "withdraw":
            accounts[name].withdraw(amount)

    for name, acc in accounts.items():
        vip_tag = " (VIP)" if (show_vip and acc.is_vip()) else ""
        print(f"{name} : {acc.balance}{vip_tag}")


# 3. Functional Programming (FP)
def run_functional(tx_list, show_vip=False):
    customers = list(dict.fromkeys(tx[0] for tx in tx_list))

    def balance_for(customer):
        customer_tx = filter(lambda tx: tx[0] == customer, tx_list)
        signed = map(lambda tx: tx[2] if tx[1] == "deposit" else -tx[2], customer_tx)
        return reduce(lambda acc, val: acc + val, signed, 0)

    balances = dict(map(lambda c: (c, balance_for(c)), customers))

    vips = set(
        map(
            lambda item: item[0],
            filter(lambda item: item[1] > 3000, balances.items())
        )
    )

    for name, balance in balances.items():
        vip_tag = " (VIP)" if (show_vip and name in vips) else ""
        print(f"{name} : {balance}{vip_tag}")


# 4. Logical Programming (LP)
def run_logical(tx_list, show_vip=False):
    # Facts: (action, person, amount)
    facts = [(action, person, amount) for person, action, amount in tx_list]
    people = list(dict.fromkeys(p for _, p, _ in facts))

    # Rules
    def total_deposits(person):
        return sum(amt for act, p, amt in facts if act == "deposit" and p == person)

    def total_withdrawals(person):
        return sum(amt for act, p, amt in facts if act == "withdraw" and p == person)

    def balance_rule(person):
        return total_deposits(person) - total_withdrawals(person)

    def vip_rule(person):
        return balance_rule(person) > 3000

    for person in people:
        bal = balance_rule(person)
        vip_tag = " (VIP)" if (show_vip and vip_rule(person)) else ""
        print(f"{person} : {bal}{vip_tag}")


def main():
    paradigms = [
        ("1. Procedural Programming", run_procedural),
        ("2. Object-Oriented Programming", run_oop),
        ("3. Functional Programming", run_functional),
        ("4. Logical Programming", run_logical),
    ]

    for title, runner in paradigms:
        print(f"\n--- {title} ---")
        runner(transactions, show_vip=False)

        print("\nBonus:")
        runner(bonus_transactions, show_vip=True)


if __name__ == "__main__":
    main()

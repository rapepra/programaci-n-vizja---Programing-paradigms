# Question 3: Smart ATM Transaction System - Logical Programming (LP)
# Approach:
# Define transactions as Facts and create logical Rules to deduce total deposits,
# total withdrawals, final balances, and VIP status.

transactions = [
    ("Alice", "deposit", 5000),
    ("Bob", "withdraw", 2000),
    ("Alice", "withdraw", 1500),
    ("Charlie", "deposit", 3000),
    ("Bob", "deposit", 4000),
    ("Alice", "withdraw", 1000),
]


# Facts: (action, person, amount)
def make_facts(tx_list):
    return [(action, person, amount) for person, action, amount in tx_list]


# Rules
def rule_total_deposits(person, facts):
    return sum(amount for action, p, amount in facts if action == "deposit" and p == person)


def rule_total_withdrawals(person, facts):
    return sum(amount for action, p, amount in facts if action == "withdraw" and p == person)


def rule_balance(person, facts):
    return rule_total_deposits(person, facts) - rule_total_withdrawals(person, facts)


def rule_is_vip(person, facts):
    return rule_balance(person, facts) > 3000


def main():
    facts = make_facts(transactions)
    people = list(dict.fromkeys(p for _, p, _ in facts))

    for person in people:
        balance = rule_balance(person, facts)
        print(f"{person} : {balance}")

    # Bonus task
    print("\nBonus:")
    bonus_transactions = transactions + [("Charlie", "deposit", 2000)]
    bonus_facts = make_facts(bonus_transactions)
    bonus_people = list(dict.fromkeys(p for _, p, _ in bonus_facts))

    for person in bonus_people:
        balance = rule_balance(person, bonus_facts)
        if rule_is_vip(person, bonus_facts):
            print(f"{person} : {balance} (VIP)")
        else:
            print(f"{person} : {balance}")


if __name__ == "__main__":
    main()

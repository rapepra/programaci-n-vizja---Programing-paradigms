"""
Assignment 1 - Question 3: Smart ATM Transaction System
Paradigm 4: Logical Programming (LP)

Approach:
In Logical Programming, we represent the problem using Facts and Rules.
- Facts represent known truths (in this case, deposit and withdrawal transactions).
- Rules define how new values are deduced from existing facts.
Here, we define rules to determine total deposits, total withdrawals,
the resulting balance, and whether a customer is VIP.
"""

transactions = [
    ("Alice", "deposit", 5000),
    ("Bob", "withdraw", 2000),
    ("Alice", "withdraw", 1500),
    ("Charlie", "deposit", 3000),
    ("Bob", "deposit", 4000),
    ("Alice", "withdraw", 1000),
]


# --- FACTS ---
# We represent facts as tuples: (action, person, amount)
def make_facts(tx_list):
    return [(action, person, amount) for person, action, amount in tx_list]


# --- RULES ---
def rule_total_deposits(person, facts):
    # Sum all amounts where the fact matches ("deposit", person, amount)
    return sum(amount for action, p, amount in facts if action == "deposit" and p == person)


def rule_total_withdrawals(person, facts):
    # Sum all amounts where the fact matches ("withdraw", person, amount)
    return sum(amount for action, p, amount in facts if action == "withdraw" and p == person)


def rule_balance(person, facts):
    # Rule: balance = total_deposits - total_withdrawals
    deposits = rule_total_deposits(person, facts)
    withdrawals = rule_total_withdrawals(person, facts)
    return deposits - withdrawals


def rule_is_vip(person, facts):
    # Rule: VIP if balance > 3000
    return rule_balance(person, facts) > 3000


def main():
    facts = make_facts(transactions)

    # Get distinct customer names from facts
    people = list(dict.fromkeys(p for _, p, _ in facts))

    # Query the balance rule for each person
    for person in people:
        balance = rule_balance(person, facts)
        print(f"{person} : {balance}")

    # Bonus: Add Charlie's extra deposit fact and check VIP rule
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

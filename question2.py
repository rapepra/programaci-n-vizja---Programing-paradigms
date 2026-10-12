"""
Assignment 1 - Question 2: Procedural Programming - Fibonacci Sequence

Approach:
This program generates the Fibonacci sequence up to a given limit using a loop.
1. The user enters a positive integer which serves as the upper limit.
2. Starting with 0 and 1, we use a while loop to generate consecutive terms (a, b = b, a + b).
3. We append terms to our list while they are less than or equal to the upper limit.
4. The sequence is printed as comma-separated values.
"""


def main():
    limit = int(input("Enter a number: "))

    sequence = []
    a, b = 0, 1

    while a <= limit:
        sequence.append(a)
        a, b = b, a + b

    # Print the sequence formatted with commas
    print("Fibonacci sequence:", ", ".join(str(num) for num in sequence))


if __name__ == "__main__":
    main()

# Question 2: Procedural Programming - Fibonacci Sequence
# Approach:
# Ask the user for a number (upper limit), then use a while loop starting with 0 and 1
# to generate Fibonacci numbers (a, b = b, a + b) until the values exceed the limit.


def main():
    limit = int(input("Enter a number: "))

    sequence = []
    a, b = 0, 1

    while a <= limit:
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", ", ".join(str(num) for num in sequence))


if __name__ == "__main__":
    main()

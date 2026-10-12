"""
Assignment 1 - Question 1: Procedural Programming - Student Grades

Approach:
This program manages student grades using procedural programming.
1. The user enters grades separated by spaces, which are parsed into a list of integers.
2. We calculate the average grade using the sum and length of the list.
3. A loop checks each grade to count how many students passed (>= 50) and failed (< 50).
4. The results are displayed according to the required format.
"""


def main():
    raw_input = input("Enter the grades of students: ")
    grades = [int(val) for val in raw_input.split()]

    if not grades:
        print("No grades were entered.")
        return

    # Calculate average grade
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)

    # Count passing and failing grades
    passed = 0
    failed = 0
    for grade in grades:
        if grade >= 50:
            passed += 1
        else:
            failed += 1

    # Output results
    print(f"Average grade: {round(average, 2)}")
    print(f"Number of students who passed: {passed}")
    print(f"Number of students who failed: {failed}")


if __name__ == "__main__":
    main()

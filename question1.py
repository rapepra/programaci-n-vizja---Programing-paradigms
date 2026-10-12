# Question 1: Procedural Programming - Student Grades
# Approach:
# Read grades from user input as space-separated values, convert them into integers,
# calculate the average grade, and loop through them to count passed (>= 50) and failed (< 50).


def main():
    raw_input = input("Enter the grades of students: ")
    grades = [int(val) for val in raw_input.split()]

    if not grades:
        print("No grades were entered.")
        return

    # Calculate average
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)

    # Count passed and failed
    passed = 0
    failed = 0
    for grade in grades:
        if grade >= 50:
            passed += 1
        else:
            failed += 1

    print(f"Average grade: {round(average, 2)}")
    print(f"Number of students who passed: {passed}")
    print(f"Number of students who failed: {failed}")


if __name__ == "__main__":
    main()

"""
Week 1 review: comparisons, conditionals, loops, and input.

Run this file from the repository root:

    python Week1_Review/control_flow_and_input.py
"""


def print_heading(title):
    """Print a simple heading so the output is easy to scan."""
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def demonstrate_comparisons():
    """Show the common comparison operators used in conditions."""
    print_heading("COMPARISONS")

    x = 1
    y = 2

    print("x:", x)
    print("y:", y)
    print("x == y:", x == y)  # Equal to
    print("x != y:", x != y)  # Not equal to
    print("x > y:", x > y)    # Greater than
    print("x < y:", x < y)    # Less than
    print("x >= y:", x >= y)  # Greater than or equal to
    print("x <= y:", x <= y)  # Less than or equal to


def demonstrate_conditionals():
    """Show how Python chooses one branch with if, elif, and else."""
    print_heading("IF / ELIF / ELSE")

    score = 82

    if score >= 90:
        print("Excellent")
    elif score >= 70:
        print("Passed")
    else:
        print("Needs practice")


def demonstrate_for_loop():
    """Use a for loop when the number of repetitions is known."""
    print_heading("FOR LOOP")

    for number in range(1, 5):
        print(number)


def demonstrate_while_loop():
    """Use a while loop when repetition depends on a condition."""
    print_heading("WHILE LOOP")

    counter = 0

    while counter < 3:
        print("Counter:", counter)
        counter += 1


def demonstrate_input():
    """Read text from the user and use it in the program."""
    print_heading("INPUT")

    name = input("Enter your name: ")
    print("Hello,", name)


def main():
    """Run all review demonstrations."""
    demonstrate_comparisons()
    demonstrate_conditionals()
    demonstrate_for_loop()
    demonstrate_while_loop()
    demonstrate_input()


if __name__ == "__main__":
    main()

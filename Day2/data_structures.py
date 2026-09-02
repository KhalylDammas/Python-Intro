"""
Run this file to see the examples:

    python data_structures.py

Python's most common built-in collection types are:

    list        Ordered, changeable, and allows duplicate values.
    tuple       Ordered, unchangeable, and allows duplicate values.
    set         Unordered, changeable, and stores only unique values.
    dictionary  Stores changeable key-value pairs; keys must be unique.

Strings are also introduced because, like lists and tuples, they are ordered
sequences. They are immutable, which means their characters cannot be changed
in place.

Read each section, predict its output, and then run the file. Exercises and an
answer key are at the bottom.
"""


def print_heading(title):
    """Print a simple heading so the program's output is easy to read."""
    print(f"\n{'=' * 12} {title} {'=' * 12}")


# ---------------------------------------------------------------------------
# 1. Strings
# ---------------------------------------------------------------------------
def demonstrate_strings():
    """Demonstrate indexing, slicing, and common string methods."""
    print_heading("STRINGS")

    company = "Lantern is a security construction company"

    # Indexes start at 0. A negative index counts from the end.
    print("First character:", company[0])
    print("Last character:", company[-1])

    # A slice uses [start:stop]. The stop position is not included.
    print("Characters 0 to 6:", company[0:7])
    print("Last 7 characters:", company[-7:])

    # Slicing with a step of -1 reverses a sequence.
    print("Reversed:", company[::-1])

    # String methods return new strings; they do not modify the original.
    print("Lowercase:", company.lower())
    print("Replace spaces:", company.replace(" ", "-"))
    print("Words:", company.split())
    print("Number of characters:", len(company))

    # Strings are immutable. This would raise a TypeError:
    # company[0] = "l"


# ---------------------------------------------------------------------------
# 2. Lists
# ---------------------------------------------------------------------------
def demonstrate_lists():
    """Demonstrate a mutable, ordered collection."""
    print_heading("LISTS")

    languages = ["Python", "JavaScript", "SQL", "Python"]
    print("Original list:", languages)
    print("First item:", languages[0])
    print("Middle items:", languages[1:3])

    # Lists are mutable: their contents can change after creation.
    languages[1] = "TypeScript"
    languages.append("Go")             # Add one item to the end.
    languages.insert(1, "Java")        # Add one item at an index.
    removed_language = languages.pop()  # Remove and return the last item.

    print("Updated list:", languages)
    print("Removed item:", removed_language)
    print("Number of items:", len(languages))
    print("Does it contain SQL?", "SQL" in languages)

    # A list comprehension builds a new list from an iterable.
    word_lengths = [len(language) for language in languages]
    print("Length of each name:", word_lengths)


# ---------------------------------------------------------------------------
# 3. Tuples
# ---------------------------------------------------------------------------
def demonstrate_tuples():
    """Demonstrate an immutable, ordered collection."""
    print_heading("TUPLES")

    location = (24.7136, 46.6753)
    latitude, longitude = location  # Tuple unpacking

    print("Location:", location)
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    # Tuples are immutable. This would raise a TypeError:
    # location[0] = 25.0

    # A one-item tuple needs a trailing comma. Without it, Python sees only
    # the value inside parentheses.
    one_item_tuple = ("Python",)
    not_a_tuple = ("Python")
    print("One-item tuple:", one_item_tuple, type(one_item_tuple))
    print("Without a comma:", not_a_tuple, type(not_a_tuple))


# ---------------------------------------------------------------------------
# 4. Sets
# ---------------------------------------------------------------------------
def demonstrate_sets():
    """Demonstrate a collection of unique values."""
    print_heading("SETS")

    numbers = {5, 15, 5, 0, 20}

    # The duplicate 5 is stored only once. Sets do not support indexing, and
    # their display order is not guaranteed, so sorted() is used for printing.
    print("Unique numbers:", sorted(numbers))
    print("Number of unique values:", len(numbers))

    numbers.add(10)
    numbers.discard(100)  # Safe even when 100 is not present.
    print("After add/discard:", sorted(numbers))

    backend = {"Python", "SQL", "Docker"}
    frontend = {"JavaScript", "HTML", "Docker"}

    print("In either set (union):", sorted(backend | frontend))
    print("In both sets (intersection):", sorted(backend & frontend))
    print("Backend only (difference):", sorted(backend - frontend))

    # {} creates an empty dictionary, not an empty set.
    empty_set = set()
    print("Empty set:", empty_set)


# ---------------------------------------------------------------------------
# 5. Dictionaries
# ---------------------------------------------------------------------------
def demonstrate_dictionaries():
    """Demonstrate a mutable mapping of keys to values."""
    print_heading("DICTIONARIES")

    company = {
        "name": "Lantern",
        "industry": "Security construction",
        "employees": 25,
    }

    # Access a value using its key.
    print("Company name:", company["name"])

    # get() is useful when a key might not exist. It can return a default
    # value instead of raising a KeyError.
    print("Country:", company.get("country", "Not provided"))

    # Dictionaries are mutable: values can be updated and new pairs added.
    company["employees"] = 30
    company["country"] = "Saudi Arabia"

    print("Updated dictionary:", company)
    print("Keys:", list(company.keys()))
    print("Values:", list(company.values()))

    print("Key-value pairs:")
    for key, value in company.items():
        print(f"  {key}: {value}")


# ---------------------------------------------------------------------------
# 6. Nested data structures
# ---------------------------------------------------------------------------
def demonstrate_nested_structures():
    """Show how collection types can be combined."""
    print_heading("NESTED STRUCTURES")

    students = [
        {"name": "Aisha", "scores": [88, 91, 95]},
        {"name": "Omar", "scores": [78, 85, 82]},
    ]

    # Start with the outer list, then access the dictionary and inner list.
    first_student = students[0]
    first_average = sum(first_student["scores"]) / len(first_student["scores"])
    print(f"{first_student['name']}'s average: {first_average:.1f}")


def demonstrate_mutability():
    """Compare assignment behavior for mutable and immutable values."""
    print_heading("MUTABILITY")

    original_list = [1, 2]
    shared_list = original_list
    shared_list[0] = 99
    print("Both names refer to the changed list:", original_list, shared_list)

    # copy() creates a separate, shallow copy of a list.
    original_list = [1, 2]
    copied_list = original_list.copy()
    copied_list[0] = 99
    print("A copy can change independently:", original_list, copied_list)


def main():
    """Run all lecture demonstrations."""
    demonstrate_strings()
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_sets()
    demonstrate_dictionaries()
    demonstrate_nested_structures()
    demonstrate_mutability()


if __name__ == "__main__":
    main()


# =============================================================================
# EXERCISES
# =============================================================================
# Try these before reading the answer key. Write your code below each question
# or in a separate file. Suggested results are given where helpful.
#
# 1. UNIQUE CHARACTERS
#    Count the unique characters in the text below. Ignore spaces and treat
#    uppercase and lowercase letters as the same.
#
#    text = "Lantern is a Security construction company"
#    Expected result: 14
#
# 2. LIST UPDATE
#    Given the list below:
#      a. Add "Docker" to the end.
#      b. Replace "HTML" with "SQL".
#      c. Remove "CSS".
#
#    skills = ["Python", "HTML", "CSS"]
#    Expected result: ["Python", "SQL", "Docker"]
#
# 3. REMOVE DUPLICATES
#    Create a new list containing each number only once, in ascending order.
#
#    numbers = [4, 2, 7, 2, 4, 9, 1]
#    Expected result: [1, 2, 4, 7, 9]
#
# 4. SET OPERATIONS
#    Find the students who attend both the Python class and the SQL class.
#
#    python_students = {"Aisha", "Omar", "Sara"}
#    sql_students = {"Omar", "Sara", "Khalid"}
#    Expected result: {"Omar", "Sara"}
#
# 5. DICTIONARY LOOKUP
#    Print the product's name and price. Use get() to print "Unknown" for a
#    missing "category" key.
#
#    product = {"name": "Keyboard", "price": 250, "in_stock": True}
#
# 6. WORD FREQUENCY
#    Build a dictionary that counts how often each word occurs.
#
#    words = ["python", "sql", "python", "docker", "sql", "python"]
#    Expected result: {"python": 3, "sql": 2, "docker": 1}
#
# 7. AVERAGE SCORES
#    For each student below, print the student's name and average score.
#
#    students = [
#        {"name": "Maha", "scores": [90, 85, 95]},
#        {"name": "Yousef", "scores": [70, 80, 75]},
#    ]
#
# 8. CHOOSE A DATA STRUCTURE
#    Choose list, tuple, set, or dictionary for each situation and explain why:
#      a. GPS coordinates that should not change
#      b. Unique email addresses
#      c. A queue of customer names where order matters
#      d. A user record containing a name, age, and email

# SOL
# The answers are


# =============================================================================
# ANSWER KEY
# =============================================================================
# The solutions are functions so they do not run with the lecture examples.
# Call a function manually when you want to check an answer.


def solution_1():
    text = "Lantern is a Security construction company"
    normalized_text = text.replace(" ", "").lower()
    unique_characters = set(normalized_text)
    print(len(unique_characters))


def solution_2():
    skills = ["Python", "HTML", "CSS"]
    skills.append("Docker")
    skills[1] = "SQL"
    skills.remove("CSS")
    print(skills)


def solution_3():
    numbers = [4, 2, 7, 2, 4, 9, 1]
    unique_numbers = sorted(set(numbers))
    print(unique_numbers)


def solution_4():
    python_students = {"Aisha", "Omar", "Sara"}
    sql_students = {"Omar", "Sara", "Khalid"}
    print(python_students & sql_students)


def solution_5():
    product = {"name": "Keyboard", "price": 250, "in_stock": True}
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Category:", product.get("category", "Unknown"))


def solution_6():
    words = ["python", "sql", "python", "docker", "sql", "python"]
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    print(frequencies)


def solution_7():
    students = [
        {"name": "Maha", "scores": [90, 85, 95]},
        {"name": "Yousef", "scores": [70, 80, 75]},
    ]

    for student in students:
        scores = student["scores"]
        average = sum(scores) / len(scores)
        print(f"{student['name']}: {average:.1f}")


# Solution 8:
#   a. tuple      Coordinates are ordered and should not change.
#   b. set        A set automatically keeps values unique.
#   c. list       A list preserves order and can be updated.
#   d. dictionary Named keys clearly describe each piece of user data.

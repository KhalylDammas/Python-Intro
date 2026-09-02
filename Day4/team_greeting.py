"""Small program used for Day 4 Git branching and pull-request practice."""


# Both conflict-demo branches deliberately edit this same line.
WELCOME_MESSAGE = "Welcome to the Python course!"


def build_greeting(name: str) -> str:
    """Return a friendly, normalized greeting for one student."""
    clean_name = name.strip()
    if not clean_name:
        clean_name = "student"
    return f"{WELCOME_MESSAGE} Hello, {clean_name}."


def main() -> None:
    """Ask for a name and display the greeting."""
    name = input("What is your name? ")
    print(build_greeting(name))


if __name__ == "__main__":
    main()

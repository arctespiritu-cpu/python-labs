"""Lab 6 - User Registry (with exception handling)
Upgrade of Lab 5: uses try/except for conversion and runtime errors,
safer dictionary access, and demonstrates else/finally.
"""

MIN_AGE = 13
MAX_AGE = 120

users = []          # list of user dictionaries
usernames = set()   # lowercase usernames for fast uniqueness checks


def is_valid_email(email):
    """Basic email check: one '@', a '.' after it, no spaces."""
    if " " in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True


def get_username():
    while True:
        username = input("Username: ").strip()
        if not username:
            print("Username cannot be blank.")
        elif " " in username:
            print("Username cannot contain spaces.")
        elif username.lower() in usernames:
            print("That username is already taken. Try another.")
        else:
            return username


def get_full_name():
    while True:
        full_name = input("Full name: ").strip()
        if full_name:
            return full_name
        print("Full name cannot be blank.")


def get_age():
    """Convert age with try/except (ValueError), re-prompt until valid."""
    attempts = 0
    while True:
        age_text = input(f"Age ({MIN_AGE}-{MAX_AGE}): ").strip()
        attempts += 1
        try:
            age = int(age_text)          # may raise ValueError
        except ValueError:
            # Runs only when conversion fails (letters, blank, decimals...)
            print("Age must be a whole number (example: 25).")
        else:
            # Runs only when NO error happened in the try block
            if MIN_AGE <= age <= MAX_AGE:
                print(f"Age accepted after {attempts} attempt(s).")
                return age
            print(f"Age must be between {MIN_AGE} and {MAX_AGE}.")


def get_email():
    while True:
        email = input("Email: ").strip()
        if is_valid_email(email):
            return email
        print("Invalid email. Example: name@example.com")


def add_user():
    print("\n--- Add User ---")
    user = {
        "username": get_username(),
        "full_name": get_full_name(),
        "age": get_age(),
        "email": get_email(),
    }
    users.append(user)
    usernames.add(user["username"].lower())
    print(f"User '{user['username']}' added.")


def print_user(user):
    """Safe printing: .get() with defaults so a missing key can't crash."""
    print(f"  Username : {user.get('username', '(missing)')}")
    print(f"  Name     : {user.get('full_name', '(missing)')}")
    print(f"  Age      : {user.get('age', '(missing)')}")
    print(f"  Email    : {user.get('email', '(missing)')}")


def list_users():
    print("\n--- All Users ---")
    if not users:
        print("No users yet.")
        return
    for i, user in enumerate(users, start=1):
        print(f"[{i}]")
        print_user(user)


def search_user():
    print("\n--- Search ---")
    query = input("Username to search: ").strip().lower()
    if not query:
        print("Search cannot be blank.")
        return

    found = None
    try:
        for user in users:
            # Skip malformed records instead of crashing
            if not isinstance(user, dict):
                continue
            name = user.get("username")
            if isinstance(name, str) and name.lower() == query:
                found = user
                break
    except TypeError as error:
        print(f"Problem reading user data: {error}")
    else:
        # Runs only if the search loop finished without an exception
        if found:
            print_user(found)
        else:
            print("No user found.")
    finally:
        # Always runs, whether or not an error happened
        print("(Search finished)")


def main():
    try:
        while True:
            print("\n=== User Registry ===")
            print("1. Add a user")
            print("2. List all users")
            print("3. Search by username")
            print("4. Exit")
            choice = input("Choose (1-4): ").strip()

            if choice == "1":
                add_user()
            elif choice == "2":
                list_users()
            elif choice == "3":
                search_user()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Enter 1, 2, 3, or 4.")
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or closed input: exit cleanly instead of a traceback
        print("\nInput ended. Goodbye!")


if __name__ == "__main__":
    main()

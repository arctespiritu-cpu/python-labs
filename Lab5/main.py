"""Lab 5 - User Registry
Stores users as dictionaries in a list, with a set of usernames
to enforce uniqueness. All validation is done without try/except.

Validation rules:
- username: not blank, no spaces, unique (case-insensitive)
- full_name: not blank
- age: digits only, between MIN_AGE and MAX_AGE
- email: no spaces, one '@', and a '.' after the '@'
"""

MIN_AGE = 13
MAX_AGE = 120

users = []          # main storage: list of user dictionaries
usernames = set()   # fast uniqueness check (stored in lowercase)


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
    while True:
        age_text = input(f"Age ({MIN_AGE}-{MAX_AGE}): ").strip()
        if not age_text.isdecimal():
            print("Age must be a whole number (digits only).")
            continue
        age = int(age_text)  # safe: already confirmed digits
        if MIN_AGE <= age <= MAX_AGE:
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
    print(f"  Username : {user['username']}")
    print(f"  Name     : {user['full_name']}")
    print(f"  Age      : {user['age']}")
    print(f"  Email    : {user['email']}")


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
    if query not in usernames:  # quick set check first
        print("No user found.")
        return
    for user in users:
        if user["username"].lower() == query:
            print_user(user)
            return


def main():
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


if __name__ == "__main__":
    main()

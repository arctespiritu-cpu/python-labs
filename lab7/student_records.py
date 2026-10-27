"""Lab 7 - File I/O and JSON Processing
Reads student names and grades from the user, saves them to JSON,
then loads the JSON file and displays formatted results.
"""
import json

FILENAME = "students.json"


def get_count():
    """Ask how many records to enter (minimum 5)."""
    while True:
        try:
            n = int(input("How many student grades would you like to enter? (min 5): "))
            if n >= 5:
                return n
            print("Please enter at least 5.")
        except ValueError:
            print("Please enter a valid number.")


def get_grade(name):
    """Ask for a valid grade between 0 and 100."""
    while True:
        try:
            grade = float(input(f"Enter grade for {name}: "))
            if 0 <= grade <= 100:
                return int(grade) if grade.is_integer() else grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def collect_records(count):
    records = []
    for i in range(1, count + 1):
        name = input(f"\nStudent {i} name: ").strip()
        while not name:
            name = input("Name cannot be empty. Student name: ").strip()
        records.append({"name": name, "grade": get_grade(name)})
    return records


def save_records(records):
    with open(FILENAME, "w") as f:
        json.dump(records, f, indent=4)
    print(f"\nSaved {len(records)} records to {FILENAME}")


def load_records():
    with open(FILENAME, "r") as f:
        return json.load(f)


def display_records(records):
    print("\nStudent Records")
    print("-" * 15)
    for r in records:
        print(f"{r['name']} - {r['grade']}")


def main():
    count = get_count()
    records = collect_records(count)
    save_records(records)
    display_records(load_records())


if __name__ == "__main__":
    main()

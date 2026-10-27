"""Lab 8 - XML Processing
Collects student names and grades, stores them in an XML file
(appending if the file already exists), then loads, parses and
displays the records.
"""
import os
import xml.etree.ElementTree as ET

FILENAME = "students.xml"


def get_count():
    """Ask how many records to enter."""
    while True:
        try:
            n = int(input("How many student grades would you like to enter? "))
            if n > 0:
                return n
            print("Please enter a number greater than 0.")
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
        records.append((name, get_grade(name)))
    return records


def save_records(records):
    """Create the XML file, or add to it if it already exists."""
    if os.path.exists(FILENAME):
        tree = ET.parse(FILENAME)
        root = tree.getroot()
        print(f"\n{FILENAME} found - adding new records to it.")
    else:
        root = ET.Element("students")
        tree = ET.ElementTree(root)
        print(f"\nCreating new file: {FILENAME}")

    for name, grade in records:
        student = ET.SubElement(root, "student")
        ET.SubElement(student, "name").text = name
        ET.SubElement(student, "grade").text = str(grade)

    ET.indent(tree, space="    ")
    tree.write(FILENAME, encoding="utf-8", xml_declaration=True)
    print(f"Saved {len(records)} new record(s) to {FILENAME}")


def load_records():
    """Load and parse the XML file into a list of (name, grade)."""
    root = ET.parse(FILENAME).getroot()
    return [(s.find("name").text, s.find("grade").text)
            for s in root.findall("student")]


def display_records(records):
    print("\nStudent Records")
    print("-" * 15)
    for name, grade in records:
        print(f"{name} - {grade}")
    print(f"\nTotal records: {len(records)}")


def main():
    while True:
        save_records(collect_records(get_count()))
        display_records(load_records())
        again = input("\nAdd another record? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

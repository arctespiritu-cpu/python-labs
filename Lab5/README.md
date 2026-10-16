# Lab 5 - User Registry

A console program that stores users and validates input before saving.

## How to run
1. Install Python 3.
2. Open a terminal in the `Lab5/` folder.
3. Run: `python main.py`
4. Pick an option from the menu (1-4).

## Validation rules
- **Username:** cannot be blank, cannot contain spaces, must be unique (case-insensitive, so `Sam` and `sam` count as the same).
- **Full name:** cannot be blank (whitespace trimmed with `.strip()`).
- **Age:** must be digits only (`.isdecimal()`), then converted to `int`, and must be between **13 and 120**.
- **Email:** no spaces, exactly one `@`, text before the `@`, and a `.` in the part after the `@` (not at the start or end).

Invalid input shows a message and re-prompts until valid. No try/except is used (per Lab 5).

## Why list + dictionary + set
- **Dictionary:** each user has named fields (`username`, `full_name`, `age`, `email`), which is clearer than remembering index positions.
- **List:** keeps all user dictionaries in the order they were added, easy to loop through for listing.
- **Set:** stores usernames so checking "is this taken?" is fast and duplicates are impossible.

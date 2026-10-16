# Lab 6 - User Registry (Exception Handling)

Upgrade of Lab 5 with try/except, safer data access, and debugging notes.

## How to run
1. Install Python 3.
2. Open a terminal in the `Lab6/` folder.
3. Run: `python main.py` (or `py main.py`)

## Exceptions handled
| Where | Exception | Why |
|---|---|---|
| `get_age()` | `ValueError` | `int()` fails on letters, blanks, decimals. Re-prompts until valid. |
| `search_user()` | `TypeError` | Protects against malformed data while looping through records. |
| `main()` | `KeyboardInterrupt`, `EOFError` | Ctrl+C or closed input exits cleanly with no traceback. |

## Safer data access
- `dict.get()` is used in `search_user()` and `print_user()` so missing keys don't crash.
- Malformed records (not a dict, username not a string) are skipped in search.

## else / finally
- `get_age()`: `else` runs the range check only when conversion succeeded.
- `search_user()`: `else` shows the result if the search had no error; `finally` always prints "(Search finished)".

## Validation rules (same as Lab 5)
- Username: not blank, no spaces, unique (case-insensitive)
- Full name: not blank
- Age: whole number between 13 and 120
- Email: no spaces, one `@`, and a `.` after the `@`

See `DEBUGGING_NOTES.txt` for the debugging reflection.

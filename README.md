# 🛠️ Python Input Validator

This project is a **Command-Line Interface (CLI) validator tool** written in Python. It validates different types of user inputs using **regular expressions (regex)** and provides **real-time feedback** using color-coded terminal output.

---

## What the Program Does

The `validator.py` script allows the user to validate five types of input data:

1. **Email addresses**
2. **Currency amounts**
3. **U.S. phone numbers**
4. **Credit card numbers**
5. **Time (12-hour or 24-hour format)**

---

## How It Works

When the script runs, it presents a **menu** to the user. Based on the user’s selection, it triggers the appropriate validation function.

Each function:
- Prompts the user for input
- Uses a **regular expression** (`re.fullmatch`) to validate the input format
- Prints the result to the console with **ANSI escape codes** for color formatting

---

## Function-by-Function Breakdown

### 1. `email_validator()`

- Prompts for an email.
- Checks the format using regex:
  - No double dots.
  - Local part allows special characters like `+`, `_`, `-`.
  - Domain must end in a valid top-level domain like `.com`, `.org`.
- Prints valid or invalid result.

### 2. `currency_amount()`

- Prompts for a currency amount in U.S. dollar format (e.g., `$1,000.00`).
- Regex ensures:
  - Starts with `$`
  - Proper comma placement for thousands
  - Optional two decimal digits
- Highlights if the format is valid or not.

### 3. `phone_number()`

- Prompts for a U.S. phone number.
- Accepts:
  - `(123) 456-7890`
  - `123-456-7890`
  - `123.456.7890`
- First extracts digits to check if there are **exactly 10 numbers**.
- Then matches formatting using regex.
- Warns the user if the digit count or format is incorrect.

### 4. `credit_card()`

- Prompts for a credit card number.
- Accepts numbers grouped by hyphens or spaces (e.g., `1234-5678-9012-3456`).
- Uses regex to check for four 4-digit groups separated by `-` or space.
- Feedback is shown in green if valid.

### 5. `validate_time()`

- Lets user choose:
  - 24-hour format (`HH:MM`)
  - 12-hour format (`HH:MM am/pm`)
- Validates time input using two separate regex patterns:
  - 24-hour: `00:00` to `23:59`
  - 12-hour: `1:00 am` to `12:59 pm`
- Gives feedback depending on correctness.

---

## Terminal Colors

The program uses **ANSI escape codes** to highlight output:

- Blue, Red, Magenta, Green backgrounds indicate different statuses
- These make validation feedback more visible and fun to use

---

## How to Run

1. Ensure Python 3 is installed.

2. Open a terminal and navigate to the script folder.

3. Run:

   ```bash
   python validator.py

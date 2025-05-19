import re

def email_validator():
    email = input("Enter your email address: \n")
    email_regex = re.compile(
        r"^(?!.*\.\.)"                     
        r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"  
        r"(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"  
        r"@"
        r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"  
        r"[a-zA-Z]{2,}$"                 
    )
    if re.fullmatch(email_regex, email):
        print(f"\033[1;44m{email}\033[0m :Valid email address")
    else:
        print(f"\033[44{email}\033[0mInvalid email address")

def currency_amount():
    amount_input = input("Enter the amount in dollars starting with a ($) sign: \n").strip()
    currency_amount_regex = re.compile(
        r"^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$"
    )
    if re.fullmatch(currency_amount_regex, amount_input):
        print(f"\033[1,41m{amount_input}\033[1;0m :Valid currency format")
    else:
        print(f"\033[1,92m{amount_input}\033[0m :Invalid currency format")

def extract_digits(s):
    return ''.join(filter(str.isdigit, s))

def phone_number():
    number = input("Enter a phone number (e.g., (123) xxx-xxxx, 123-xxx-xxxx, 123.xxx.xxxx): \n").strip()
    digits = extract_digits(number)

    if len(digits) != 10:
        print(f"\033[1;95m{number}\033[0m: Invalid: Your number has {len(digits)} digits. A U.S. phone number must have exactly 10.")
        return

    phone_regex = re.compile(
        r'^(\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}$'
    )

    if re.fullmatch(phone_regex, number):
        print(f"\033[1;43m{number}\033[0m: Valid phone number")
    else:
        print(f"\033[1;44m{number}\033[0m:Invalid phone number format. Use one of these formats.")
        print("   - (123) xxx-xxxx")
        print("   - 123-xxx-xxxx")
        print("   - 123.xxx.xxxx")

def credit_card():
    card = input("Enter your credit card number (format: XXXX-XXXXX-XXXX-XXXX): \n").strip()
    card_regex = re.compile(r'^\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}$')
    if re.fullmatch(card_regex, card):
        print(f"\033[1;32m{card}\033[0m :Valid credit card format")
    else:
        print(f"\033[44m{card}\033[0mInvalid credit card number format")
def validate_time():
    print("\nChoose the time format to validate:")
    print("1. 24-hour format")
    print("2. 12-hour format, indicate am/pm")
    choice = input("Enter 1 or 2: ").strip()

    time_input = input("Enter the time: ").strip().lower()

    # 24-hour time regex
    time_24 = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d$')
    # 12-hour time regex
    time_12 = re.compile(r'^(0?[1-9]|1[0-2]):[0-5]\d\s?(am|pm)$')
    if choice == '1':
        if re.fullmatch(time_24, time_input):
            print("Valid 24-hour time format")
        else:
            print("Invalid 24-hour format.")
    elif choice == '2':
        if re.fullmatch(time_12, time_input):
            print("Valid 12-hour time format")
        else:
            print(f"\033[44m{time_input}\033[0mInvalid 12-hour format.")
    else:
        print("Invalid option. Please enter 1 or 2.")

def main():
    print("\033[1;91m<'-'>>>>>>>>>>\033[1;4;5;32mWELCOME TO THE VALIDATOR!\033[0;1;91m<<<<<<<<<'-'>\033[0m")
    while True:
        print("\n  \033[1;34m[-------------Menu----------------]\033[0m")
        print("  | 1. Validate Email Address       |")
        print("  | 2. Validate Currency Amount     |")
        print("  | 3. Validate Phone Number        |")
        print("  | 4. Validate Credit Card Number  |")
        print("  | 5. Validate Time                |")
        print("  | 6. Exit                         |")
        print("  \033[1;34m[---------------------------------]\033[0m")
        print("><-----Please select an option from the menu:-----><")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            email_validator()
        elif choice == '2':
            currency_amount()
        elif choice == '3':
            phone_number()
        elif choice == '4':
            credit_card()
        elif choice == '5':
            validate_time()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

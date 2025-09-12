def get_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip().title()
        if value and not value.isdigit():
            return value
        print("Invalid input! Please enter text only.")

def get_digits(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Invalid input! Please enter digits only.")

def get_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Invalid input! Please enter an integer.")

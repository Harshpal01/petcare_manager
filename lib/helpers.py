from datetime import datetime

def input_int(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if allow_empty and value == '':
            return None
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_date(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if allow_empty and value == '':
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")

def input_string(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if allow_empty and value == '':
            return None
        if value:
            return value
        print("Input cannot be empty.")

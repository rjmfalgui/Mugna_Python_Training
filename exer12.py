import re

def is_valid_phone_number(value):
    valid_format = "^(\+63)\d{10}$"
    result = re.match(valid_format, value)

    if result:
        print("Format valid!")
    else:
        print("Invalid format!")

user_input = input("Enter number: ")
is_valid_phone_number(user_input)
import re        # use regular expressions/regex
import secrets   # 
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
    alphabets = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_characters = alphabets + numbers + symbols

    while True:
        password = ""
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [(nums, r'\d'), # \d is a shorthand for [0-9]
                       (lowercase, r'[a-z]'),
                       (uppercase, r'[A-Z]'),
                       (special_chars, fr'[{symbols}]') 
                       # fr'[{symbols}]' safely builds a regex character class from dynamic input while preserving special characters
                       ]
                        # Check constraints
    
    return password

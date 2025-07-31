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
                       (special_chars, r'\W') # \W is a shorthand for [^a-zA-Z0-9_]
                       ]
    
    return password

# Check generated password meets the criteria
# A character class is indicated by square brackets
pattern = r'\.'
quote = "Not all those who wander are lost."
print(re.findall(pattern, quote))
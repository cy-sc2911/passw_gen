import secrets
import string

def generate_password(length):
    alphabets = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_characters = alphabets + numbers + symbols

    password = ""
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
    return password

print(generate_password(8))
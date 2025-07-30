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
        constraints = [(nums, " ")]
    
    return password

# The re.compile() function compiles the string passed as
# the arugment into a regular expression object that
# can be used by other 're' methods
# the '+' quantifier means it should repeat one or more times
pattern = re.compile('l+')
quote = "Not all those who wander are lost."
print(pattern.search(quote))
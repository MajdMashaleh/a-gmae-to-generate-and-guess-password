import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True, include_uppercase=True, include_lowercase=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def analyze_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if length < 8 and not (has_upper  and has_digit and has_symbol):
        return "Weak"
    elif length > 14 and  (has_upper and has_lower and has_digit and has_symbol):
        return "Strong"
    else:
        return "Medium"


def main():
    print("\nWelcome to the Advanced Password Generator!")

    while True:
        length = int(input("Enter the desired password length: "))
        
        # Prompt for uppercase letters inclusion
        while True:
            include_uppercase = input("Include uppercase letters? (yes/no): ").lower()
            if include_uppercase == "yes" or include_uppercase == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Prompt for lowercase letters inclusion
        while True:
            include_lowercase = input("Include lowercase letters? (yes/no): ").lower()
            if include_lowercase == "yes" or include_lowercase == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Prompt for digits inclusion
        while True:
            include_digits = input("Include digits? (yes/no): ").lower()
            if include_digits == "yes" or include_digits == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Prompt for symbols inclusion
        while True:
            include_symbols = input("Include symbols? (yes/no): ").lower()
            if include_symbols == "yes" or include_symbols == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        password = generate_password(length, include_digits == "yes", include_symbols == "yes", include_uppercase == "yes", include_lowercase == "yes")
        print("Generated Password:", password)

        strength = analyze_password_strength(password)
        print("Password Strength:", strength)

        generate_another = input("Generate another password? (yes/no): ").lower()
        if generate_another != "yes":
            break


if __name__ == "__main__":
    main()

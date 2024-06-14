import random
import string

def generate_password(name_included, pet_included, nickname_included):
    # Initialize empty list to store user choices
    choices = []
    
    # Add name, pet's name, and nickname if included
    if name_included:
        choices.append(input("Enter your name: "))
    if pet_included:
        choices.append(input("Enter your pet's name: "))
    if nickname_included:
        choices.append(input("Enter your nickname: "))

    while True:
        try:
            char_count = int(input("How many additional characters do you want in your password? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Generate password with random characters
    random_chars = ''
    for _ in range(char_count):
        random_chars += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    # Combine user choices and random characters
    password = ''.join(choices) + random_chars
    
    return password

def analyze_password_strength(password, name_included, pet_included, nickname_included):
    if name_included and not pet_included and not nickname_included:
        return "Weak"
    elif name_included and (pet_included or nickname_included):
        return "Medium"
    elif pet_included and nickname_included:
        return "Strong"

# Main program
if __name__ == "__main__":
    while True:
        name_included = input("Do you want to include your name in the password? (yes/no): ").lower() == "yes"
        pet_included = input("Do you want to include your pet's name in the password? (yes/no): ").lower() == "yes"
        nickname_included = input("Do you want to include your nickname in the password? (yes/no): ").lower() == "yes"

        password = generate_password(name_included, pet_included, nickname_included)
        print("Your generated password is:", password)

        # Analyze password strength based on the inclusion of name, pet's name, and nickname
        strength = analyze_password_strength(password, name_included, pet_included, nickname_included)
        print("Password Strength:", strength)

        generate_another = input("Do you want to generate another password? (yes/no): ").lower()
        if generate_another != "yes":
            break

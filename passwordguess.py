import string

def brute_force_attack(actual_password):
    charset = string.ascii_letters + string.digits + string.punctuation
    password_length = len(actual_password)
    attempts = 0

    # Initialize an empty string to store the current guess
    current_guess = ''

    # Iterate over each character position in the password
    for i in range(password_length):
        found = False
        # Iterate over each character in the charset
        for char in charset:
            attempts += 1
            current_guess = current_guess[:i] + char + current_guess[i+1:]
            print("Attempt {}: {}".format(attempts, current_guess))
            # Check if the current character matches the actual password
            if current_guess[i] == actual_password[i]:
                found = True
                break  # Move to the next character position
        if not found:
            return None, attempts

    return current_guess, attempts

while True:
    # Example password to guess
    actual_password = input("Enter the password to guess: ")

    # Perform brute-force attack
    password_found, total_attempts = brute_force_attack(actual_password)

    # Check if the password was found
    if password_found:
        print("Password cracked: ", password_found)
        print("Total attempts:", total_attempts)
    else:
        print("Password not found within the given charset.")

    generate_another = input("guess another password? (yes/no): ").lower()
    if generate_another != "yes":
        break

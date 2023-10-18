import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    if length < 8:
        return "Password length should be at least 8 characters."

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print("Generated Password: " + password)
    except ValueError:
        print("Invalid input. Please enter a valid password length (an integer).")

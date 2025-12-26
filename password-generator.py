import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generate a random password based on specified criteria.
    
    Parameters:
    - length: Length of the password
    - use_uppercase: Include uppercase letters (A-Z)
    - use_lowercase: Include lowercase letters (a-z)
    - use_digits: Include digits (0-9)
    - use_symbols: Include special symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
    
    Returns:
    - Generated password string
    """
    char_pool = ""
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    
    if not char_pool:
        return "Error: At least one character type must be selected!"
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("=" * 50)
    print("        PASSWORD GENERATOR")
    print("=" * 50)
    print()
    
    try:
        # Get password length from user
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Error: Password length must be greater than 0!")
            return
        
        # Ask user for password complexity options
        print("\nPassword Complexity Options:")
        print("(Press Enter for default 'yes' or type 'no' to exclude)")
        
        use_uppercase = input("Include uppercase letters (A-Z)? [yes]: ").strip().lower() != 'no'
        use_lowercase = input("Include lowercase letters (a-z)? [yes]: ").strip().lower() != 'no'
        use_digits = input("Include digits (0-9)? [yes]: ").strip().lower() != 'no'
        use_symbols = input("Include symbols (!@#$...)? [yes]: ").strip().lower() != 'no'
        
        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        
        # Display the generated password
        print("\n" + "=" * 50)
        print("Your Generated Password:")
        print("=" * 50)
        print(f"\n  {password}\n")
        print("=" * 50)
        print("\nPassword generated successfully!")
        print("Make sure to store it in a secure location.")
        
    except ValueError:
        print("Error: Please enter a valid number for password length!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

import random
import string
import secrets

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generate a cryptographically secure random password.
    
    Parameters:
    - length: Length of the password
    - use_uppercase: Include uppercase letters (A-Z)
    - use_lowercase: Include lowercase letters (a-z)
    - use_digits: Include digits (0-9)
    - use_symbols: Include special symbols
    
    Returns:
    - Generated password string
    """
    char_pool = ""
    guaranteed_chars = []
    
    # Build character pool and guarantee at least one from each selected type
    if use_uppercase:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        guaranteed_chars.append(secrets.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        guaranteed_chars.append(secrets.choice(string.punctuation))
    
    if not char_pool:
        return None
    
    # If password is shorter than guaranteed chars, just use random selection
    if length < len(guaranteed_chars):
        password = ''.join(secrets.choice(char_pool) for _ in range(length))
    else:
        # Fill remaining length with random characters
        remaining_length = length - len(guaranteed_chars)
        password_list = guaranteed_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]
        
        # Shuffle to avoid predictable pattern
        random.shuffle(password_list)
        password = ''.join(password_list)
    
    return password

def calculate_strength(password, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Calculate and return password strength assessment."""
    length = len(password)
    char_types = sum([use_uppercase, use_lowercase, use_digits, use_symbols])
    
    # Calculate pool size
    pool_size = 0
    if use_uppercase: pool_size += 26
    if use_lowercase: pool_size += 26
    if use_digits: pool_size += 10
    if use_symbols: pool_size += 32
    
    # Entropy calculation: log2(pool_size^length)
    import math
    entropy = length * math.log2(pool_size) if pool_size > 0 else 0
    
    # Determine strength
    if entropy < 28:
        strength = "WEAK"
        color = "⚠️"
    elif entropy < 36:
        strength = "FAIR"
        color = "⚡"
    elif entropy < 60:
        strength = "GOOD"
        color = "✓"
    elif entropy < 128:
        strength = "STRONG"
        color = "✓✓"
    else:
        strength = "VERY STRONG"
        color = "✓✓✓"
    
    return strength, entropy, color

def display_password_info(password, length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Display password with detailed information."""
    strength, entropy, color = calculate_strength(password, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    print("\n" + "=" * 60)
    print("                   GENERATED PASSWORD")
    print("=" * 60)
    print(f"\n  PASSWORD: {password}\n")
    print("=" * 60)
    print(f"  Length: {length} characters")
    print(f"  Strength: {color} {strength}")
    print(f"  Entropy: {entropy:.1f} bits")
    print("=" * 60)
    
    # Character composition
    char_types = []
    if use_uppercase: char_types.append("Uppercase")
    if use_lowercase: char_types.append("Lowercase")
    if use_digits: char_types.append("Digits")
    if use_symbols: char_types.append("Symbols")
    
    print(f"  Contains: {', '.join(char_types)}")
    print("=" * 60)
    print("\n💡 Security Tips:")
    print("  • Never reuse passwords across different accounts")
    print("  • Store in a secure password manager")
    print("  • Change passwords periodically")
    print("  • Enable two-factor authentication when available")
    print()

def main():
    print("\n" + "=" * 60)
    print("                  PASSWORD GENERATOR v2.0")
    print("=" * 60)
    print("\n  Generate strong, secure passwords with custom options\n")
    
    while True:
        try:
            # Get password length
            length = int(input("Enter desired password length (minimum 4): "))
            
            if length < 4:
                print("❌ Error: Password length must be at least 4 characters!\n")
                continue
            
            if length > 128:
                confirm = input(f"⚠️  {length} characters is very long. Continue? (yes/no): ")
                if confirm.lower() != 'yes':
                    continue
            
            # Password complexity options
            print("\n" + "-" * 60)
            print("  PASSWORD COMPLEXITY OPTIONS")
            print("-" * 60)
            print("  (Press Enter for 'yes' or type 'no' to exclude)\n")
            
            use_uppercase = input("  Include uppercase letters (A-Z)? [yes]: ").strip().lower() != 'no'
            use_lowercase = input("  Include lowercase letters (a-z)? [yes]: ").strip().lower() != 'no'
            use_digits = input("  Include digits (0-9)? [yes]: ").strip().lower() != 'no'
            use_symbols = input("  Include symbols (!@#$%^&*...)? [yes]: ").strip().lower() != 'no'
            
            # Validate at least one option is selected
            if not any([use_uppercase, use_lowercase, use_digits, use_symbols]):
                print("\n❌ Error: You must select at least one character type!\n")
                continue
            
            # Generate password
            print("\n🔄 Generating secure password...")
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
            
            if password is None:
                print("❌ Error: Unable to generate password!\n")
                continue
            
            # Display results
            display_password_info(password, length, use_uppercase, use_lowercase, use_digits, use_symbols)
            
            # Ask if user wants to generate another
            print("=" * 60)
            another = input("\nGenerate another password? (yes/no): ").strip().lower()
            if another != 'yes':
                print("\n✓ Thank you for using Password Generator v2.0!")
                print("  Stay secure! 🔒\n")
                break
            
            print("\n")
            
        except ValueError:
            print("❌ Error: Please enter a valid number!\n")
        except KeyboardInterrupt:
            print("\n\n✓ Password Generator closed. Stay secure! 🔒\n")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()

def get_valid_key():
    """Prompt the user to input a valid key for Caesar cipher."""
    while True:
        try:
            key = int(input("Enter the key (an integer): "))
            if key < 0:
                print("Key must be a non-negative integer. Please try again.")
            else:
                return key
        except ValueError:
            print("Invalid input. Please enter an integer.")

def encrypt_decrypt(text, mode, key):
    """Encrypt or decrypt a text using Caesar cipher."""
    result = ''
    for char in text:
        if char.isalpha():
            shift = key if mode == 'e' else -key
          
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
           
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char  
    return result

def main():
    while True:
        print("\n*** CAESAR CIPHER PROGRAM ***")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nENCRYPTION MODE")
            key = get_valid_key()
            text = input('Enter the text to encrypt: ')
            ciphertext = encrypt_decrypt(text, 'e', key)
            print(f'CIPHERTEXT: {ciphertext}')

        elif choice == '2':
            print("\nDECRYPTION MODE")
            key = get_valid_key()
            text = input('Enter the text to decrypt: ')
            plaintext = encrypt_decrypt(text, 'd', key)
            print(f'PLAINTEXT: {plaintext}')

        elif choice == '3':
            print("Thank you for using the Caesar Cipher program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

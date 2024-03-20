def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # To ensure shift is within the range
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):# 122 in ascii
                    shifted -= 26
                elif shifted < ord('a'):# 97 in ascii
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):# 90 in ascii
                    shifted -= 26
                elif shifted < ord('A'):# 65 in ascii
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
def main():
    while True:
        choice = input("Choose operation:\n1. Encrypt\n2. Decrypt\n3. Exit \nEnter your choice : ")

        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted_message = caesar_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted_message = caesar_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

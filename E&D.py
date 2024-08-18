def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            code_point = ord(char)
            base = ord('a') if char.islower() else ord('A')
            new_char = chr(base + (code_point - base + shift_amount) % 26)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        print("\nCaesar Cipher - Encryption and Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option! Please choose again.")

if __name__ == "__main__":
    main()

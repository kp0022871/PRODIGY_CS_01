def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift_amount) %26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift_amount) %26) + ord('A'))
        else:
            encrypted_text += char 
    return encrypted_text
def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)
choice = input("Enter 'E' to encrypt and 'D' to decrypt: ").upper()
if choice=='E':
    text = input("Enter text to encrypt: ")
    shift = int(input("Shift key: "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted text: ", encrypted_text)
elif choice=='D':
    text = input("Enter text to decrypt: ")
    shift = int(input("Shift key: "))
    decrypted_text = caesar_cipher_decrypt(text, shift)
    print("Encrypted text: ", decrypted_text)
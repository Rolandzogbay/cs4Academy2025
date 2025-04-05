# This code implements a Caesar cipher encryption and decryption algorithm.
def caesar_cipher(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
        
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

plain_text = "Hello world"
shifted_value = 3
cipher_text = caesar_cipher(plain_text, shifted_value)

print(f"Encrypted text: {cipher_text}")

# print(f"Decrypted text: {caesar_cipher(cipher_text, -shifted_value)}")
# This code implements a Caesar cipher encryption and decryption algorithm.
    
        

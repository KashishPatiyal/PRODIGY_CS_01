def encrypt(PT, key):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    CT = ""
    for char in PT:
        if char in alphabets:
            index = (alphabets.index(char) + key) % len(alphabets)
            CT += alphabets[index]
        else:
            CT += char  # Non-alphabetic characters remain unchanged
    return CT

def decrypt(CT, key):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PT = ""
    for char in CT:
        if char in alphabets:
            index = (alphabets.index(char) - key) % len(alphabets)
            PT += alphabets[index]
        else:
            PT += char  # Non-alphabetic characters remain unchanged
    return PT

# Input
PT = input("Enter the text to be encrypted: ").upper()
key = int(input("Enter the key (numeric value): "))

# Encrypt
cipher_text = encrypt(PT, key)
print("Encrypted text:", cipher_text)

# Decrypt
plain_text = decrypt(cipher_text, key)
print("Decrypted text:", plain_text)
 

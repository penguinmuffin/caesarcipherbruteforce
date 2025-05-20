# Cipher text to be decrypted
cipher_text = ""
for shift in range(26):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decrypted += char
    print(f"Shift {shift}: {decrypted}")

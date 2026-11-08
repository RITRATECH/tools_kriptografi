def vigenere_encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()

    # Perpanjang key agar panjangnya sama dengan plaintext
    full_key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    
    ciphertext = ''
    for p, k in zip(plaintext, full_key):
        p_index = alphabet.index(p)
        k_index = alphabet.index(k)
        c_index = (p_index + k_index) % 26
        ciphertext += alphabet[c_index]
    
    return ciphertext

# Contoh penggunaan:
plaintext = "MYPROJECTUASS"
key = "KRIPTOGRAFIAES"

cipher = vigenere_encrypt(plaintext, key)
print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", cipher)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

plaintext = "MY PROJECT UASS  ".encode('utf-8')
key = "KRIPTOGRAFIAESKU".encode('utf-8')

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, 16))

print("Cipher (hex):", binascii.hexlify(ciphertext).decode())

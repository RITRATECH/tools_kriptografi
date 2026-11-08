from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

key = "KRIPTOGRAFIAESKU".encode('utf-8')
ciphertext = binascii.unhexlify("a19c6feb2328a8559bc2398546ea6ab643cd99d02a89a365fd205459f2889134")

cipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(cipher.decrypt(ciphertext), 16)
print("Decrypted:", decrypted.decode('utf-8'))

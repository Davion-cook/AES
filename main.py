from functions.aes_encrypt import aes_encrypt

message        = "HELLO_AES_123456"
encryption_key = "THISISASECRETKEY"

cipher_state = aes_encrypt(message, encryption_key)

print("Ciphertext state:")
for row in cipher_state:
    print([hex(b) for b in row])

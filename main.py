from functions.aes_encrypt import aes_encrypt
from functions.text_convert import bytes_to_text

message        = "HELLO_AES_123456"
encryption_key = "THISISASECRETKEY"

cipher_state = aes_encrypt(message, encryption_key)

print("Ciphertext state:")
for row in cipher_state:
    print([hex(b) for b in row])

# Flatten state column-major and convert UTF-8 values back to characters
flat_bytes = [cipher_state[row][col] for col in range(4) for row in range(4)]
ciphertext = bytes_to_text(flat_bytes)
print("Ciphertext string:", ciphertext)

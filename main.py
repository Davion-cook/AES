from functions import text_convert
from functions import bytes_to_state
from functions import state_to_hexa
from functions.key_expansion import key_expansion
import os

message = "HELLO_AES_123456"
bytes_data = text_convert.text_to_bytes(message)

print(bytes_data)


state = bytes_to_state.bytes_to_state(bytes_data)

for row in state:
    print(row)

hex_state = state_to_hexa.state_to_hex(state)

for row in hex_state:
    print(row)

key = key_expansion(bytes_data)

for word in key:
    print(word)
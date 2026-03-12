from functions import text_convert
from functions import bytes_to_state

message = "HELLO_AES_123456"
bytes_data = text_convert.text_to_bytes(message)

print(bytes_data)


state = bytes_to_state.bytes_to_state(bytes_data)

for row in state:
    print(row)


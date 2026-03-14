from functions import text_convert
from functions import bytes_to_state
from functions import state_to_hexa
from functions.key_expansion import key_expansion
from functions.add_round_key import add_round_key
import os

message = "HELLO_AES_123456"
encryption_key = "THISISASECRETKEY"  

bytes_data = text_convert.text_to_bytes(message)
key_bytes = text_convert.text_to_bytes(encryption_key)

#print(bytes_data)

state = bytes_to_state.bytes_to_state(bytes_data)
print(f"state: {state}")

#for row in state:
 #   print(row)

# hex_state = state_to_hexa.state_to_hex(state)

#for row in hex_state:
#    print(row)

key = key_expansion(key_bytes)


# Extract the initial round key (words 0-3)
round_key_0 = key[0:4]


# Apply AddRoundKey with the initial round key
new_state = add_round_key(state, round_key_0)

print("State after AddRoundKey (round 0):")
for row in new_state:
    print(row)

#--------------------
org_new_state = add_round_key(new_state, round_key_0)

print("State after AddRoundKey (round 0):")
for row in org_new_state:
    print(row)
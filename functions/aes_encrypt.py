from functions.text_convert import text_to_bytes
from functions.bytes_to_state import bytes_to_state
from functions.key_expansion import key_expansion
from functions.add_round_key import add_round_key
from functions.sub_byte import sub_bytes
from functions.shift_row import shift_rows
from functions.mix_columns import mix_columns


def aes_encrypt(message, key):
    """
    AES-128 Encryption — FIPS 197 Section 5.1

    Encrypts a 16-character plaintext message with a 16-character key
    using the full 10-round AES-128 cipher.

    Inputs:
        message — 16-character plaintext string
        key     — 16-character key string

    Output:
        4x4 state matrix of ints representing the ciphertext
    """
    # Convert inputs to bytes and build state/round keys
    message_bytes = text_to_bytes(message)
    key_bytes = text_to_bytes(key)

    state = bytes_to_state(message_bytes)
    expanded_key = key_expansion(key_bytes)

    # Round 0: initial AddRoundKey
    state = add_round_key(state, expanded_key[0:4])

    # Rounds 1–9: SubBytes → ShiftRows → MixColumns → AddRoundKey
    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, expanded_key[r*4 : r*4+4])

    # Round 10 (final): SubBytes → ShiftRows → AddRoundKey (no MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, expanded_key[40:44])

    return state

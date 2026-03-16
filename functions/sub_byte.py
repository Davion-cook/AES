import os
import json

def load_sbox():
    """
    Load SBOX from aes_con.json.
    Looks one folder up from this file (same as key_expansion.py).
    """
    folder   = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(folder, "../data/aes_con.json")

    with open(filepath, "r") as f:
        data = json.load(f)

    return data["SBOX"]


SBOX = load_sbox()


def sub_bytes(state):
    """
    SubBytes — FIPS 197 Section 5.1.1

    Applies the AES S-box independently to every byte in the state.
    Each byte value (0–255) is used as an index into the S-box table,
    and the corresponding value replaces it.

    Input:
        state — 4x4 matrix of ints (values 0–255)

    Output:
        new 4x4 state matrix after S-box substitution
    """
    new_state = []

    for row in state:
        new_row = []
        for byte in row:
            new_row.append(SBOX[byte])
        new_state.append(new_row)

    return new_state
# ── Load constants from JSON ──────────────────
import os
import json

def load_constants():
    """
    Load SBOX and RCON from aes_constants.json.
    Looks for the file in the same folder as this script.
    """
    folder   = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(folder, "../data/aes_con.json")
 
    with open(filepath, "r") as f:
        data = json.load(f)
 
    return data["SBOX"], data["RCON"]
 
 
SBOX, RCON = load_constants()


# rotate the word in the vector by 1 postion to the left
def rot_word(word):

    return [word[1], word[2], word[3], word[0]]
 
 
# S-box lookup function
def sub_word(word):
    """
    Apply the S-box to each of the 4 bytes in a word.
    Used inside key expansion — same S-box as SubBytes.
    """
    return [SBOX[byte] for byte in word]
 
 
# ── Helper 3 ──────────────────────────────────
def xor_words(word_a, word_b):
    """
    XOR two 4-byte words together, byte by byte.
    Returns a new 4-byte word.
    """
    return [a ^ b for a, b in zip(word_a, word_b)]
 
 
# ── Main function ─────────────────────────────
def key_expansion(key):
    """
    Expand a 16-byte key into 44 words (11 round keys).
 
    Input : key — list of 16 ints (your raw key bytes)
    Output: w   — list of 44 words, each word is a list of 4 ints
 
    Round key for round n = words w[4n], w[4n+1], w[4n+2], w[4n+3]
    """
 
    w = []  # will hold all 44 words when done
 
    # ── Step 1: load the original key as the first 4 words ──
    # Each word is 4 consecutive bytes from the key
    for i in range(4):
        word = [key[4 * i],
                key[4 * i + 1],
                key[4 * i + 2],
                key[4 * i + 3]]
        w.append(word)
 
    # ── Step 2: derive words 4 through 43 ──
    for i in range(4, 44):
        temp = w[i - 1]  # start from the previous word
 
        if i % 4 == 0:
            # Every 4th word gets the special treatment:
            #   1. Rotate left by 1 byte
            #   2. Sub each byte through S-box
            #   3. XOR with round constant Rcon[i // 4]
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp = xor_words(temp, RCON[i // 4])
 
        # All words: XOR temp with the word 4 positions back
        new_word = xor_words(w[i - 4], temp)
        w.append(new_word)
 
    return w  # 44 words tota
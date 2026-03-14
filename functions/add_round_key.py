def add_round_key(state, round_key):
    """
    AddRoundKey — FIPS 197 Section 5.1.4

    XORs each column of the state with the corresponding word
    from the round key.

    Inputs:
        state     — 4x4 matrix of ints  (state[row][col])
        round_key — list of 4 words, each word is a list of 4 ints
                    i.e. w[4*round .. 4*round+3] from key_expansion()

    Output:
        new 4x4 state matrix after XOR
    """
    new_state = []
    for row in range(4):
        new_row = []
        for col in range(4):
            # round_key[col] is the word for this column
            # round_key[col][row] is the matching byte in that word
            new_byte = state[row][col] ^ round_key[col][row]
            new_row.append(new_byte)
        new_state.append(new_row)

    return new_state


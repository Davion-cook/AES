def shift_rows(state):
    """
    ShiftRows — FIPS 197 Section 5.1.2

    Cyclically shifts each row of the state to the left by its row index:
        Row 0 — no shift
        Row 1 — shift left by 1
        Row 2 — shift left by 2
        Row 3 — shift left by 3

    Input:
        state — 4x4 matrix of ints

    Output:
        new 4x4 state matrix after row shifts
    """
    new_state = []

    for row_index, row in enumerate(state):
        shifted_row = row[row_index:] + row[:row_index]
        new_state.append(shifted_row)

    return new_state
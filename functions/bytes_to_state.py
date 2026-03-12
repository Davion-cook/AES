
def bytes_to_state(bytes_data):
    # Create empty 4x4 state matrix
    state = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    # Index to track position in bytes_data
    byte_index = 0

    # Loop over columns first (AES is column-major)
    for col in range(4):
        # Loop over rows inside each column
        for row in range(4):
            state[row][col] = bytes_data[byte_index]
            byte_index += 1

    return state

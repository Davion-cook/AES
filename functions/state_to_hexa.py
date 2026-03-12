def state_to_hex(state):
    
    # Convert a 4x4 AES state matrix from decimal to hex strings.
    
    hex_state = []

    for row in state:
        hex_row = []
        for byte in row:
            hex_row.append(f"{byte:02X}")
        hex_state.append(hex_row)

    return hex_state
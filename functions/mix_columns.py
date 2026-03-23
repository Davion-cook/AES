def xtime(a):
    """
    Multiply a byte by 2 in GF(2^8).
    Left-shift by 1; if the high bit was set, XOR with 0x1b (the irreducible polynomial).
    """
    if a & 0x80:
        return ((a << 1) ^ 0x1b) & 0xFF
    return (a << 1) & 0xFF


def gmul(a, b):
    """
    Multiply two bytes in GF(2^8) using the Russian peasant algorithm.
    """
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1b
        b >>= 1
    return result


def mix_columns(state):
    """
    MixColumns — FIPS 197 Section 5.1.3

    Treats each column of the state as a polynomial over GF(2^8) and
    multiplies it by the fixed polynomial a(x) = {03}x^3 + {01}x^2 + {01}x + {02}.

    Each column [s0, s1, s2, s3] is transformed as:
        s0' = (2*s0) ^ (3*s1) ^ s2 ^ s3
        s1' = s0 ^ (2*s1) ^ (3*s2) ^ s3
        s2' = s0 ^ s1 ^ (2*s2) ^ (3*s3)
        s3' = (3*s0) ^ s1 ^ s2 ^ (2*s3)

    Input:
        state — 4x4 matrix of ints (state[row][col])

    Output:
        new 4x4 state matrix after MixColumns
    """
    new_state = [[0] * 4 for _ in range(4)]

    for col in range(4):
        s0 = state[0][col]
        s1 = state[1][col]
        s2 = state[2][col]
        s3 = state[3][col]

        new_state[0][col] = gmul(2, s0) ^ gmul(3, s1) ^ s2       ^ s3
        new_state[1][col] = s0          ^ gmul(2, s1) ^ gmul(3, s2) ^ s3
        new_state[2][col] = s0          ^ s1          ^ gmul(2, s2) ^ gmul(3, s3)
        new_state[3][col] = gmul(3, s0) ^ s1          ^ s2          ^ gmul(2, s3)

    return new_state

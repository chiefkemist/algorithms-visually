"""Hacker's Delight Section 3-2: Rounding to Powers of 2 — Solutions"""

MASK32 = 0xFFFFFFFF

def round_up_to_pow2(x):
    """clp2: round up to next power of 2."""
    if x == 0:
        return 0
    x = (x - 1) & MASK32
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return (x + 1) & MASK32

def round_down_to_pow2(x):
    """flp2: round down to previous power of 2."""
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return x - (x >> 1)

def floor_log2(x):
    """Floor of log base 2 (position of highest set bit)."""
    assert x > 0
    n = 0
    if x >= (1 << 16): n += 16; x >>= 16
    if x >= (1 << 8):  n += 8;  x >>= 8
    if x >= (1 << 4):  n += 4;  x >>= 4
    if x >= (1 << 2):  n += 2;  x >>= 2
    if x >= (1 << 1):  n += 1
    return n


if __name__ == "__main__":
    assert round_up_to_pow2(0) == 0
    assert round_up_to_pow2(1) == 1
    assert round_up_to_pow2(2) == 2
    assert round_up_to_pow2(3) == 4
    assert round_up_to_pow2(5) == 8
    assert round_up_to_pow2(8) == 8
    assert round_up_to_pow2(9) == 16
    assert round_up_to_pow2(13) == 16
    assert round_up_to_pow2(200) == 256
    assert round_up_to_pow2(0x80000000) == 0x80000000

    assert round_down_to_pow2(0) == 0
    assert round_down_to_pow2(1) == 1
    assert round_down_to_pow2(2) == 2
    assert round_down_to_pow2(3) == 2
    assert round_down_to_pow2(5) == 4
    assert round_down_to_pow2(8) == 8
    assert round_down_to_pow2(13) == 8
    assert round_down_to_pow2(200) == 128
    assert round_down_to_pow2(0xFFFFFFFF) == 0x80000000

    assert floor_log2(1) == 0
    assert floor_log2(2) == 1
    assert floor_log2(3) == 1
    assert floor_log2(8) == 3
    assert floor_log2(15) == 3
    assert floor_log2(16) == 4
    assert floor_log2(200) == 7
    assert floor_log2(0xFFFFFFFF) == 31

    print("All round_to_power tests passed!")

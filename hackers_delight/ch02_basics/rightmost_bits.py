"""Chapter 2, Section 2-1: Manipulating Rightmost Bits

These are the fundamental building blocks of bit manipulation.
Each function operates on a single 32-bit unsigned word.

Reference: "Hacker's Delight" 2nd Ed., pp. 11-15

Instructions: Implement each function using ONLY bitwise operations
and arithmetic (+, -, &, |, ^, ~). No loops, no branches.
Each function should be a single expression.

Note: Use MASK32 = 0xFFFFFFFF to keep results within 32-bit unsigned range.
"""

MASK32 = 0xFFFFFFFF


def turn_off_lowest_bit(x):
    """Turn off the rightmost 1-bit in x.

    Example: 0b01011000 -> 0b01010000
             0b00000001 -> 0b00000000

    Hint: involves (x - 1)
    Use: test if x is a power of 2 (result == 0 means yes)
    """
    raise NotImplementedError("TODO: implement turn_off_lowest_bit")


def turn_on_lowest_zero_bit(x):
    """Turn on the rightmost 0-bit in x.

    Example: 0b10100111 -> 0b10101111
             0b01010100 -> 0b01010101

    Hint: involves (x + 1)
    """
    raise NotImplementedError("TODO: implement turn_on_lowest_zero_bit")


def isolate_lowest_bit(x):
    """Isolate the rightmost 1-bit (all other bits become 0).

    Example: 0b01011000 -> 0b00001000
             0b01010100 -> 0b00000100

    Hint: involves negation
    Use: Fenwick trees, memory allocators, finding lowest priority
    """
    raise NotImplementedError("TODO: implement isolate_lowest_bit")


def isolate_lowest_zero_bit(x):
    """Isolate the rightmost 0-bit (result has a single 1 where x had its rightmost 0).

    Example: 0b10100111 -> 0b00001000
             0b11111110 -> 0b00000001

    Hint: involves complement (~x)
    """
    raise NotImplementedError("TODO: implement isolate_lowest_zero_bit")


def mask_from_lowest_bit(x):
    """Create a mask from the rightmost 1-bit down through all trailing zeros.

    Example: 0b01011000 -> 0b00001111
             0b01010100 -> 0b00000111
             0b00000001 -> 0b00000001

    Hint: involves (x - 1) and XOR
    """
    raise NotImplementedError("TODO: implement mask_from_lowest_bit")


def turn_off_trailing_ones(x):
    """Turn off trailing 1-bits.

    Example: 0b10100111 -> 0b10100000
             0b11111111 -> 0b00000000
             0b10101000 -> 0b10101000 (no trailing 1s, unchanged)

    Hint: involves (x + 1)
    Use: test if x is of the form 2^n - 1 (result == 0 means yes)
    """
    raise NotImplementedError("TODO: implement turn_off_trailing_ones")


def turn_on_trailing_zeros(x):
    """Turn on trailing 0-bits.

    Example: 0b10101000 -> 0b10101111
             0b01010111 -> 0b01010111 (no trailing 0s, unchanged)

    Hint: involves (x - 1)
    """
    raise NotImplementedError("TODO: implement turn_on_trailing_zeros")


def is_power_of_two(x):
    """Test if x is a power of 2 (exactly one bit set).
    Returns False for 0, True for 1, 2, 4, 8, ...

    Hint: a power of 2 has exactly one bit set;
          turning off that bit gives zero.
    """
    raise NotImplementedError("TODO: implement is_power_of_two")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # turn_off_lowest_bit
    assert turn_off_lowest_bit(0b01011000) == 0b01010000
    assert turn_off_lowest_bit(0b01010100) == 0b01010000
    assert turn_off_lowest_bit(0b00000001) == 0
    assert turn_off_lowest_bit(0x80000000) == 0
    assert turn_off_lowest_bit(0b11111111) == 0b11111110
    assert turn_off_lowest_bit(0) == 0
    assert turn_off_lowest_bit(16) == 0
    assert turn_off_lowest_bit(1024) == 0

    # turn_on_lowest_zero_bit
    assert turn_on_lowest_zero_bit(0b10100111) == 0b10101111
    assert turn_on_lowest_zero_bit(0b01010100) == 0b01010101
    assert turn_on_lowest_zero_bit(0b00000000) == 0b00000001
    assert turn_on_lowest_zero_bit(0b01111111) == 0b11111111
    assert turn_on_lowest_zero_bit(0x7FFFFFFF) == 0xFFFFFFFF

    # isolate_lowest_bit
    assert isolate_lowest_bit(0b01011000) == 0b00001000
    assert isolate_lowest_bit(0b01010100) == 0b00000100
    assert isolate_lowest_bit(0b11111111) == 0b00000001
    assert isolate_lowest_bit(0) == 0
    assert isolate_lowest_bit(64) == 64
    assert isolate_lowest_bit(0b10101010) == 2

    # isolate_lowest_zero_bit
    assert isolate_lowest_zero_bit(0b10100111) == 0b00001000
    assert isolate_lowest_zero_bit(0b11111110) == 0b00000001
    assert isolate_lowest_zero_bit(0) == 0b00000001
    assert isolate_lowest_zero_bit(0b11111101) == 0b00000010
    assert isolate_lowest_zero_bit(0xFFFFFFFF) == 0

    # mask_from_lowest_bit
    assert mask_from_lowest_bit(0b01011000) == 0b00001111
    assert mask_from_lowest_bit(0b01010100) == 0b00000111
    assert mask_from_lowest_bit(0b11111111) == 0b00000001
    assert mask_from_lowest_bit(0b00000001) == 0b00000001
    assert mask_from_lowest_bit(0x80000000) == 0xFFFFFFFF
    # Edge case: x=0 has no rightmost 1-bit; formula yields all-ones
    assert mask_from_lowest_bit(0) == 0xFFFFFFFF

    # turn_off_trailing_ones
    assert turn_off_trailing_ones(0b10100111) == 0b10100000
    assert turn_off_trailing_ones(0b11111111) == 0
    assert turn_off_trailing_ones(0b10101000) == 0b10101000
    assert turn_off_trailing_ones(0) == 0
    assert turn_off_trailing_ones(0xFFFFFFFF) == 0

    # turn_on_trailing_zeros
    assert turn_on_trailing_zeros(0b10101000) == 0b10101111
    assert turn_on_trailing_zeros(0b01010111) == 0b01010111
    assert turn_on_trailing_zeros(0) == 0xFFFFFFFF
    assert turn_on_trailing_zeros(0b11111111) == 0b11111111
    assert turn_on_trailing_zeros(0x80000000) == 0xFFFFFFFF

    # is_power_of_two
    assert not is_power_of_two(0)
    assert is_power_of_two(1)
    assert is_power_of_two(2)
    assert is_power_of_two(4)
    assert is_power_of_two(1024)
    assert is_power_of_two(0x80000000)
    assert not is_power_of_two(3)
    assert not is_power_of_two(6)
    assert not is_power_of_two(255)
    assert not is_power_of_two(0xFFFFFFFF)

    print("All rightmost_bits tests passed!")

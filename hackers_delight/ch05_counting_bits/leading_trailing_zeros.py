"""Chapter 5, Sections 5-3 and 5-4: Counting Leading and Trailing Zeros

Count the number of leading (from MSB) or trailing (from LSB) zero bits.

Reference: "Hacker's Delight" 2nd Ed., pp. 99-109

Instructions: Implement using binary search (checking half the word
at a time, then a quarter, etc.) or using popcount tricks.

Note: Use MASK32 = 0xFFFFFFFF to keep results within 32-bit unsigned range.
"""

MASK32 = 0xFFFFFFFF


def count_leading_zeros(x):
    """Count leading zeros (number of 0-bits before the first 1-bit from the left).

    Example: count_leading_zeros(0)          == 32
             count_leading_zeros(1)          == 31
             count_leading_zeros(0x80000000) == 0
             count_leading_zeros(0xFF)       == 24

    Hint (binary search approach): if the top 16 bits are zero, add 16 to count
    and shift left by 16. Then check the top 8, add 8 if zero, shift. Repeat
    for 4, 2, 1.
    """
    raise NotImplementedError("TODO: implement count_leading_zeros")


def count_trailing_zeros(x):
    """Count trailing zeros (number of 0-bits after the last 1-bit from the right).

    Example: count_trailing_zeros(0)          == 32
             count_trailing_zeros(1)          == 0
             count_trailing_zeros(0x80000000) == 31
             count_trailing_zeros(0b01011000) == 3

    Hint: ntz(x) = 32 - popcount(x | (x - 1)), or
          ntz(x) = popcount(~x & (x - 1))
    """
    raise NotImplementedError("TODO: implement count_trailing_zeros")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # count_leading_zeros
    assert count_leading_zeros(0) == 32
    assert count_leading_zeros(1) == 31
    assert count_leading_zeros(0x80000000) == 0
    assert count_leading_zeros(0xFF) == 24
    assert count_leading_zeros(0xFFFF) == 16
    assert count_leading_zeros(0xFFFFFFFF) == 0
    assert count_leading_zeros(0b1010) == 28
    assert count_leading_zeros(0x40000000) == 1

    # count_trailing_zeros
    assert count_trailing_zeros(0) == 32
    assert count_trailing_zeros(1) == 0
    assert count_trailing_zeros(0x80000000) == 31
    assert count_trailing_zeros(0xFF) == 0
    assert count_trailing_zeros(0b01011000) == 3
    assert count_trailing_zeros(0xFFFFFFFF) == 0
    assert count_trailing_zeros(0b10110000) == 4
    assert count_trailing_zeros(12) == 2

    print("All leading_trailing_zeros tests passed!")

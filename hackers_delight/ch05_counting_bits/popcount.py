"""Chapter 5, Section 5-1: Population Count (Hamming Weight)

Count the number of 1-bits in a word. Also known as "popcount"
or "Hamming weight."

Reference: "Hacker's Delight" 2nd Ed., pp. 81-96

Instructions: Implement the divide-and-conquer version that
processes bits in parallel -- pairs, nibbles, bytes, halfwords, word.
Use the magic constants 0x55555555, 0x33333333, 0x0F0F0F0F, etc.

Note: Use MASK32 = 0xFFFFFFFF to keep results within 32-bit unsigned range.
"""

MASK32 = 0xFFFFFFFF


def popcount(x):
    """Count the number of 1-bits in x using divide-and-conquer.

    Example: popcount(0b00000000) == 0
             popcount(0b11111111) == 8
             popcount(0b10101010) == 4
             popcount(0xFFFFFFFF) == 32

    Hint: sum adjacent pairs, then nibbles, then bytes, then halfwords.
      Step 1: x = (x & 0x55555555) + ((x >> 1) & 0x55555555)  -- pairs
      Step 2: x = (x & 0x33333333) + ((x >> 2) & 0x33333333)  -- nibbles
      Step 3: ... continue doubling the group size
    """
    raise NotImplementedError("TODO: implement popcount")


def popcount_naive(x):
    """Naive loop-based popcount for comparison.
    Count bits by checking and shifting one at a time.

    Hint: loop 32 times, check lowest bit with (x & 1), shift right.
    """
    raise NotImplementedError("TODO: implement popcount_naive")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # popcount
    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(0x80000000) == 1
    assert popcount(0xFF) == 8
    assert popcount(0xFFFF) == 16
    assert popcount(0xFFFFFFFF) == 32
    assert popcount(0b10101010) == 4
    assert popcount(0x55555555) == 16
    assert popcount(0xAAAAAAAA) == 16
    assert popcount(0b10110000) == 3

    # popcount_naive
    assert popcount_naive(0) == 0
    assert popcount_naive(1) == 1
    assert popcount_naive(0xFFFFFFFF) == 32
    assert popcount_naive(0b10101010) == 4
    assert popcount_naive(0x55555555) == 16
    assert popcount_naive(0b10110000) == 3

    print("All popcount tests passed!")

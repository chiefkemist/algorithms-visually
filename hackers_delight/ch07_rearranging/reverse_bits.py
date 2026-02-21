"""Chapter 7, Section 7-1: Reversing Bits and Bytes

Reverse the bit order of a word using recursive swap:
swap halves, then quarters, then eighths, etc.

Reference: "Hacker's Delight" 2nd Ed., pp. 129-134

Instructions: Use mask-shift-OR to swap at each level.
Five steps: swap adjacent bits, pairs, nibbles, bytes, halfwords.

Note: Use MASK32 = 0xFFFFFFFF to keep results within 32-bit unsigned range.
"""

MASK32 = 0xFFFFFFFF


def reverse_bits(x):
    """Reverse all 32 bits of x (bit 0 becomes bit 31, etc.).

    Example: reverse_bits(0b00000001) == 0x80000000
             reverse_bits(0xB0000000) == 0x0000000D

    Hint: five steps with masks 0x55555555, 0x33333333, 0x0F0F0F0F, 0x00FF00FF:
      Step 1: swap adjacent bits       (1-bit groups)
      Step 2: swap adjacent pairs      (2-bit groups)
      Step 3: swap adjacent nibbles    (4-bit groups)
      Step 4: swap adjacent bytes      (8-bit groups)
      Step 5: swap halfwords           (16-bit groups)
    """
    raise NotImplementedError("TODO: implement reverse_bits")


def reverse_bytes(x):
    """Reverse the byte order of x (byte 0 becomes byte 3, etc.).

    Example: reverse_bytes(0x12345678) == 0x78563412
             reverse_bytes(0x000000FF) == 0xFF000000

    Hint: only the last two steps of reverse_bits (swap bytes, swap halfwords),
          or shift-and-mask directly.
    """
    raise NotImplementedError("TODO: implement reverse_bytes")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # reverse_bits
    assert reverse_bits(0) == 0
    assert reverse_bits(1) == 0x80000000
    assert reverse_bits(0x80000000) == 1
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF
    assert reverse_bits(0x0000000F) == 0xF0000000
    assert reverse_bits(0xF0000000) == 0x0000000F
    # Palindrome: 0b1001...1001
    assert reverse_bits(0xAAAAAAAA) == 0x55555555
    assert reverse_bits(0x55555555) == 0xAAAAAAAA

    # reverse_bytes
    assert reverse_bytes(0) == 0
    assert reverse_bytes(0x12345678) == 0x78563412
    assert reverse_bytes(0x000000FF) == 0xFF000000
    assert reverse_bytes(0xFF000000) == 0x000000FF
    assert reverse_bytes(0xFFFFFFFF) == 0xFFFFFFFF
    assert reverse_bytes(1) == 0x01000000
    assert reverse_bytes(0xDEADBEEF) == 0xEFBEADDE

    print("All reverse_bits tests passed!")

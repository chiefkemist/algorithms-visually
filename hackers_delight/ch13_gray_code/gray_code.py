"""Chapter 13: Gray Code

Gray code is a binary encoding where consecutive values differ
in exactly one bit. This minimizes transition errors in hardware
(rotary encoders, ADC) and creates smooth motion patterns.

Reference: "Hacker's Delight" 2nd Ed., pp. 311-318

Instructions: binary_to_gray is a single expression.
gray_to_binary requires a parallel prefix XOR (multiple steps).

Note: Use MASK32 = 0xFFFFFFFF to keep results within 32-bit unsigned range.
"""

MASK32 = 0xFFFFFFFF


def binary_to_gray(x):
    """Convert a standard binary number to Gray code.

    Example: binary_to_gray(0) == 0
             binary_to_gray(1) == 1
             binary_to_gray(2) == 3  (0b10 -> 0b11)
             binary_to_gray(3) == 2  (0b11 -> 0b10)
             binary_to_gray(4) == 6  (0b100 -> 0b110)

    Hint: a single XOR with a shifted version of x.
    """
    raise NotImplementedError("TODO: implement binary_to_gray")


def gray_to_binary(g):
    """Convert a Gray code number back to standard binary.

    Example: gray_to_binary(0) == 0
             gray_to_binary(1) == 1
             gray_to_binary(3) == 2  (0b11 -> 0b10)
             gray_to_binary(2) == 3  (0b10 -> 0b11)
             gray_to_binary(6) == 4  (0b110 -> 0b100)

    Hint: parallel prefix XOR. XOR g with shifted versions of itself:
      g ^= (g >> 1); g ^= (g >> 2); g ^= (g >> 4); ... up to >> 16
    """
    raise NotImplementedError("TODO: implement gray_to_binary")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # binary_to_gray
    assert binary_to_gray(0) == 0
    assert binary_to_gray(1) == 1
    assert binary_to_gray(2) == 3
    assert binary_to_gray(3) == 2
    assert binary_to_gray(4) == 6
    assert binary_to_gray(5) == 7
    assert binary_to_gray(6) == 5
    assert binary_to_gray(7) == 4
    assert binary_to_gray(8) == 12
    # Full byte: 0xFF -> 0x80
    assert binary_to_gray(0xFF) == 0x80

    # gray_to_binary
    assert gray_to_binary(0) == 0
    assert gray_to_binary(1) == 1
    assert gray_to_binary(3) == 2
    assert gray_to_binary(2) == 3
    assert gray_to_binary(6) == 4
    assert gray_to_binary(7) == 5
    assert gray_to_binary(5) == 6
    assert gray_to_binary(4) == 7
    assert gray_to_binary(12) == 8
    assert gray_to_binary(0x80) == 0xFF

    # roundtrip: binary -> gray -> binary
    for i in range(256):
        assert gray_to_binary(binary_to_gray(i)) == i

    # gray code: consecutive values differ by one bit
    for i in range(255):
        g1 = binary_to_gray(i)
        g2 = binary_to_gray(i + 1)
        diff = g1 ^ g2
        # diff should be a power of 2 (exactly one bit different)
        assert diff != 0 and (diff & (diff - 1)) == 0

    print("All gray_code tests passed!")

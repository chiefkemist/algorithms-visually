"""Chapter 3, Section 3-2: Rounding to a Power of 2

Round integers up or down to the nearest power of 2.
The technique: right-propagate the highest set bit (the "bit flood"),
then adjust.

Reference: "Hacker's Delight" 2nd Ed., pp. 59-66

Instructions: Implement using shifts and OR to flood bits rightward.
No loops needed -- five shift+OR steps cover all 32 bits.

Note: Use MASK32 = 0xFFFFFFFF to keep results within 32-bit unsigned range.
"""

MASK32 = 0xFFFFFFFF


def round_up_to_pow2(x):
    """Round up to the next power of 2 (or return x if already a power of 2).
    Returns 0 for input 0.

    Example: round_up_to_pow2(5)  == 8
             round_up_to_pow2(8)  == 8
             round_up_to_pow2(1)  == 1
             round_up_to_pow2(13) == 16

    Hint: subtract 1, then flood rightward with OR-shifts (1, 2, 4, 8, 16),
          then add 1.
    """
    raise NotImplementedError("TODO: implement round_up_to_pow2")


def round_down_to_pow2(x):
    """Round down to the previous power of 2 (or return x if already a power of 2).
    Returns 0 for input 0.

    Example: round_down_to_pow2(5)  == 4
             round_down_to_pow2(8)  == 8
             round_down_to_pow2(13) == 8
             round_down_to_pow2(1)  == 1

    Hint: flood rightward with OR-shifts, then subtract half.
    """
    raise NotImplementedError("TODO: implement round_down_to_pow2")


def floor_log2(x):
    """Floor of log base 2 (position of the highest set bit, 0-indexed).
    Undefined for input 0.

    Example: floor_log2(1)  == 0
             floor_log2(8)  == 3
             floor_log2(15) == 3
             floor_log2(16) == 4

    Hint: use round_down_to_pow2 or a binary search approach.
    """
    raise NotImplementedError("TODO: implement floor_log2")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # round_up_to_pow2
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

    # round_down_to_pow2
    assert round_down_to_pow2(0) == 0
    assert round_down_to_pow2(1) == 1
    assert round_down_to_pow2(2) == 2
    assert round_down_to_pow2(3) == 2
    assert round_down_to_pow2(5) == 4
    assert round_down_to_pow2(8) == 8
    assert round_down_to_pow2(13) == 8
    assert round_down_to_pow2(200) == 128
    assert round_down_to_pow2(0xFFFFFFFF) == 0x80000000

    # floor_log2
    assert floor_log2(1) == 0
    assert floor_log2(2) == 1
    assert floor_log2(3) == 1
    assert floor_log2(8) == 3
    assert floor_log2(15) == 3
    assert floor_log2(16) == 4
    assert floor_log2(200) == 7
    assert floor_log2(0xFFFFFFFF) == 31

    print("All round_to_power tests passed!")

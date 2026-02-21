"""Chapter 2, Section 2-4: Absolute Value Function

Branchless absolute value using bit manipulation.
The key insight: arithmetic right shift of a signed integer by 31
produces a mask that is all-0s for positive, all-1s for negative.

Reference: "Hacker's Delight" 2nd Ed., pp. 18-19

Instructions: Implement using ONLY bitwise operations and arithmetic.
No if/else, no ternary, no branches. Each should be 1-2 expressions.

Note: Use ctypes.c_int32 to emulate signed 32-bit arithmetic in Python.
"""

import ctypes


def _to_i32(x):
    """Ensure x is treated as a signed 32-bit integer."""
    return ctypes.c_int32(x).value


def branchless_abs(x):
    """Branchless absolute value.

    Example: branchless_abs(5)  == 5
             branchless_abs(-5) == 5
             branchless_abs(0)  == 0

    Hint: arithmetic right shift by 31 creates a mask:
      positive numbers -> mask = 0x00000000 (all zeros)
      negative numbers -> mask = 0xFFFFFFFF (all ones)
    Then XOR with the mask and subtract the mask.
    """
    raise NotImplementedError("TODO: implement branchless_abs")


def branchless_nabs(x):
    """Branchless negative absolute value (always returns <= 0).

    Example: branchless_nabs(5)  == -5
             branchless_nabs(-5) == -5
             branchless_nabs(0)  == 0

    Hint: similar to branchless_abs but with the operations inverted.
    Advantage: nabs(INT_MIN) is well-defined, while abs(INT_MIN) overflows.
    """
    raise NotImplementedError("TODO: implement branchless_nabs")


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":
    # branchless_abs
    assert branchless_abs(0) == 0
    assert branchless_abs(1) == 1
    assert branchless_abs(-1) == 1
    assert branchless_abs(42) == 42
    assert branchless_abs(-42) == 42
    assert branchless_abs(2147483647) == 2147483647
    assert branchless_abs(-2147483647) == 2147483647

    # branchless_nabs
    assert branchless_nabs(0) == 0
    assert branchless_nabs(1) == -1
    assert branchless_nabs(-1) == -1
    assert branchless_nabs(42) == -42
    assert branchless_nabs(-42) == -42
    assert branchless_nabs(2147483647) == -2147483647
    assert branchless_nabs(-2147483647) == -2147483647
    # nabs(INT_MIN) is well-defined:
    assert branchless_nabs(-2147483648) == -2147483648

    print("All absolute_value tests passed!")

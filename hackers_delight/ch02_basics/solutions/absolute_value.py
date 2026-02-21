"""Hacker's Delight Section 2-4: Absolute Value Function — Solutions"""

import ctypes

def _to_i32(x):
    """Ensure x is treated as a signed 32-bit integer."""
    return ctypes.c_int32(x).value

def branchless_abs(x):
    """y = x >> 31; (x ^ y) - y"""
    x = _to_i32(x)
    y = x >> 31
    return _to_i32((x ^ y) - y)

def branchless_nabs(x):
    """y = x >> 31; y - (x ^ y)"""
    x = _to_i32(x)
    y = x >> 31
    return _to_i32(y - (x ^ y))


if __name__ == "__main__":
    assert branchless_abs(0) == 0
    assert branchless_abs(1) == 1
    assert branchless_abs(-1) == 1
    assert branchless_abs(42) == 42
    assert branchless_abs(-42) == 42
    assert branchless_abs(2147483647) == 2147483647
    assert branchless_abs(-2147483647) == 2147483647

    assert branchless_nabs(0) == 0
    assert branchless_nabs(1) == -1
    assert branchless_nabs(-1) == -1
    assert branchless_nabs(42) == -42
    assert branchless_nabs(-42) == -42
    assert branchless_nabs(2147483647) == -2147483647
    assert branchless_nabs(-2147483647) == -2147483647
    assert branchless_nabs(-2147483648) == -2147483648

    print("All absolute_value tests passed!")

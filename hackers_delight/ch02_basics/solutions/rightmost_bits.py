"""Hacker's Delight Section 2-1: Manipulating Rightmost Bits — Solutions"""

MASK32 = 0xFFFFFFFF

def turn_off_lowest_bit(x):
    """x & (x - 1)"""
    return (x & (x - 1)) & MASK32

def turn_on_lowest_zero_bit(x):
    """x | (x + 1)"""
    return (x | (x + 1)) & MASK32

def isolate_lowest_bit(x):
    """x & (-x)"""
    return (x & (-x)) & MASK32

def isolate_lowest_zero_bit(x):
    """~x & (x + 1)"""
    return (~x & (x + 1)) & MASK32

def mask_from_lowest_bit(x):
    """x ^ (x - 1)"""
    return (x ^ (x - 1)) & MASK32

def turn_off_trailing_ones(x):
    """x & (x + 1)"""
    return (x & (x + 1)) & MASK32

def turn_on_trailing_zeros(x):
    """x | (x - 1)"""
    return (x | (x - 1)) & MASK32

def is_power_of_two(x):
    """x != 0 and x & (x - 1) == 0"""
    return x != 0 and (x & (x - 1)) == 0


if __name__ == "__main__":
    # turnOffLowestBit
    assert turn_off_lowest_bit(0b01011000) == 0b01010000
    assert turn_off_lowest_bit(0b01010100) == 0b01010000
    assert turn_off_lowest_bit(0b00000001) == 0
    assert turn_off_lowest_bit(0x80000000) == 0
    assert turn_off_lowest_bit(0b11111111) == 0b11111110
    assert turn_off_lowest_bit(0) == 0

    # turnOnLowestZeroBit
    assert turn_on_lowest_zero_bit(0b10100111) == 0b10101111
    assert turn_on_lowest_zero_bit(0b01010100) == 0b01010101
    assert turn_on_lowest_zero_bit(0) == 1
    assert turn_on_lowest_zero_bit(0b01111111) == 0b11111111
    assert turn_on_lowest_zero_bit(0x7FFFFFFF) == 0xFFFFFFFF

    # isolateLowestBit
    assert isolate_lowest_bit(0b01011000) == 0b00001000
    assert isolate_lowest_bit(0b01010100) == 0b00000100
    assert isolate_lowest_bit(0b11111111) == 1
    assert isolate_lowest_bit(0) == 0
    assert isolate_lowest_bit(64) == 64
    assert isolate_lowest_bit(0b10101010) == 2

    # isolateLowestZeroBit
    assert isolate_lowest_zero_bit(0b10100111) == 0b00001000
    assert isolate_lowest_zero_bit(0b11111110) == 1
    assert isolate_lowest_zero_bit(0) == 1
    assert isolate_lowest_zero_bit(0b11111101) == 0b00000010
    assert isolate_lowest_zero_bit(0xFFFFFFFF) == 0

    # maskFromLowestBit
    assert mask_from_lowest_bit(0b01011000) == 0b00001111
    assert mask_from_lowest_bit(0b01010100) == 0b00000111
    assert mask_from_lowest_bit(0b11111111) == 1
    assert mask_from_lowest_bit(1) == 1
    assert mask_from_lowest_bit(0x80000000) == 0xFFFFFFFF
    assert mask_from_lowest_bit(0) == 0xFFFFFFFF

    # turnOffTrailingOnes
    assert turn_off_trailing_ones(0b10100111) == 0b10100000
    assert turn_off_trailing_ones(0b11111111) == 0
    assert turn_off_trailing_ones(0b10101000) == 0b10101000
    assert turn_off_trailing_ones(0) == 0
    assert turn_off_trailing_ones(0xFFFFFFFF) == 0

    # turnOnTrailingZeros
    assert turn_on_trailing_zeros(0b10101000) == 0b10101111
    assert turn_on_trailing_zeros(0b01010111) == 0b01010111
    assert turn_on_trailing_zeros(0) == 0xFFFFFFFF
    assert turn_on_trailing_zeros(0b11111111) == 0b11111111
    assert turn_on_trailing_zeros(0x80000000) == 0xFFFFFFFF

    # isPowerOfTwo
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

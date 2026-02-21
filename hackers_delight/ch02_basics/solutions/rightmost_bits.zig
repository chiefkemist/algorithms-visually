const std = @import("std");
const expect = std.testing.expect;

/// Turn off the rightmost 1-bit: x & (x - 1)
pub fn turnOffLowestBit(x: u32) u32 {
    return x & (x -% 1);
}

/// Turn on the rightmost 0-bit: x | (x + 1)
pub fn turnOnLowestZeroBit(x: u32) u32 {
    return x | (x +% 1);
}

/// Isolate the rightmost 1-bit: x & (-x)
pub fn isolateLowestBit(x: u32) u32 {
    return x & (0 -% x);
}

/// Isolate the rightmost 0-bit: ~x & (x + 1)
pub fn isolateLowestZeroBit(x: u32) u32 {
    return ~x & (x +% 1);
}

/// Mask from the rightmost 1-bit through trailing zeros: x ^ (x - 1)
pub fn maskFromLowestBit(x: u32) u32 {
    return x ^ (x -% 1);
}

/// Turn off trailing 1's: x & (x + 1)
pub fn turnOffTrailingOnes(x: u32) u32 {
    return x & (x +% 1);
}

/// Turn on trailing 0's: x | (x - 1)
pub fn turnOnTrailingZeros(x: u32) u32 {
    return x | (x -% 1);
}

/// Test if power of two: x != 0 and x & (x - 1) == 0
pub fn isPowerOfTwo(x: u32) bool {
    return x != 0 and (x & (x -% 1)) == 0;
}

test "turnOffLowestBit" {
    try expect(turnOffLowestBit(0b01011000) == 0b01010000);
    try expect(turnOffLowestBit(0b01010100) == 0b01010000);
    try expect(turnOffLowestBit(0b00000001) == 0);
    try expect(turnOffLowestBit(0x80000000) == 0);
    try expect(turnOffLowestBit(0b11111111) == 0b11111110);
    try expect(turnOffLowestBit(0) == 0);
}

test "turnOnLowestZeroBit" {
    try expect(turnOnLowestZeroBit(0b10100111) == 0b10101111);
    try expect(turnOnLowestZeroBit(0b01010100) == 0b01010101);
    try expect(turnOnLowestZeroBit(0) == 1);
    try expect(turnOnLowestZeroBit(0b01111111) == 0b11111111);
    try expect(turnOnLowestZeroBit(0x7FFFFFFF) == 0xFFFFFFFF);
}

test "isolateLowestBit" {
    try expect(isolateLowestBit(0b01011000) == 0b00001000);
    try expect(isolateLowestBit(0b01010100) == 0b00000100);
    try expect(isolateLowestBit(0b11111111) == 1);
    try expect(isolateLowestBit(0) == 0);
    try expect(isolateLowestBit(64) == 64);
    try expect(isolateLowestBit(0b10101010) == 2);
}

test "isolateLowestZeroBit" {
    try expect(isolateLowestZeroBit(0b10100111) == 0b00001000);
    try expect(isolateLowestZeroBit(0b11111110) == 1);
    try expect(isolateLowestZeroBit(0) == 1);
    try expect(isolateLowestZeroBit(0b11111101) == 0b00000010);
    try expect(isolateLowestZeroBit(0xFFFFFFFF) == 0);
}

test "maskFromLowestBit" {
    try expect(maskFromLowestBit(0b01011000) == 0b00001111);
    try expect(maskFromLowestBit(0b01010100) == 0b00000111);
    try expect(maskFromLowestBit(0b11111111) == 1);
    try expect(maskFromLowestBit(1) == 1);
    try expect(maskFromLowestBit(0x80000000) == 0xFFFFFFFF);
    try expect(maskFromLowestBit(0) == 0xFFFFFFFF);
}

test "turnOffTrailingOnes" {
    try expect(turnOffTrailingOnes(0b10100111) == 0b10100000);
    try expect(turnOffTrailingOnes(0b11111111) == 0);
    try expect(turnOffTrailingOnes(0b10101000) == 0b10101000);
    try expect(turnOffTrailingOnes(0) == 0);
    try expect(turnOffTrailingOnes(0xFFFFFFFF) == 0);
}

test "turnOnTrailingZeros" {
    try expect(turnOnTrailingZeros(0b10101000) == 0b10101111);
    try expect(turnOnTrailingZeros(0b01010111) == 0b01010111);
    try expect(turnOnTrailingZeros(0) == 0xFFFFFFFF);
    try expect(turnOnTrailingZeros(0b11111111) == 0b11111111);
    try expect(turnOnTrailingZeros(0x80000000) == 0xFFFFFFFF);
}

test "isPowerOfTwo" {
    try expect(!isPowerOfTwo(0));
    try expect(isPowerOfTwo(1));
    try expect(isPowerOfTwo(2));
    try expect(isPowerOfTwo(4));
    try expect(isPowerOfTwo(1024));
    try expect(isPowerOfTwo(0x80000000));
    try expect(!isPowerOfTwo(3));
    try expect(!isPowerOfTwo(6));
    try expect(!isPowerOfTwo(255));
    try expect(!isPowerOfTwo(0xFFFFFFFF));
}

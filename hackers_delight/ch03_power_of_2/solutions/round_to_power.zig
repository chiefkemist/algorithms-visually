const std = @import("std");
const expect = std.testing.expect;

/// Round up to next power of 2 (clp2). Returns 0 for input 0.
pub fn roundUpToPow2(val: u32) u32 {
    if (val == 0) return 0;
    var x = val -% 1;
    x |= x >> 1;
    x |= x >> 2;
    x |= x >> 4;
    x |= x >> 8;
    x |= x >> 16;
    return x +% 1;
}

/// Round down to previous power of 2 (flp2). Returns 0 for input 0.
pub fn roundDownToPow2(val: u32) u32 {
    var x = val;
    x |= x >> 1;
    x |= x >> 2;
    x |= x >> 4;
    x |= x >> 8;
    x |= x >> 16;
    return x - (x >> 1);
}

/// Floor of log base 2 (position of highest set bit, 0-indexed).
/// Undefined for input 0.
pub fn floorLog2(x: u32) u5 {
    std.debug.assert(x != 0);
    var n: u5 = 0;
    var v = x;
    if (v >= (1 << 16)) { n += 16; v >>= 16; }
    if (v >= (1 << 8))  { n += 8;  v >>= 8; }
    if (v >= (1 << 4))  { n += 4;  v >>= 4; }
    if (v >= (1 << 2))  { n += 2;  v >>= 2; }
    if (v >= (1 << 1))  { n += 1; }
    return n;
}

test "roundUpToPow2" {
    try expect(roundUpToPow2(0) == 0);
    try expect(roundUpToPow2(1) == 1);
    try expect(roundUpToPow2(2) == 2);
    try expect(roundUpToPow2(3) == 4);
    try expect(roundUpToPow2(5) == 8);
    try expect(roundUpToPow2(8) == 8);
    try expect(roundUpToPow2(9) == 16);
    try expect(roundUpToPow2(13) == 16);
    try expect(roundUpToPow2(200) == 256);
    try expect(roundUpToPow2(0x80000000) == 0x80000000);
}

test "roundDownToPow2" {
    try expect(roundDownToPow2(0) == 0);
    try expect(roundDownToPow2(1) == 1);
    try expect(roundDownToPow2(2) == 2);
    try expect(roundDownToPow2(3) == 2);
    try expect(roundDownToPow2(5) == 4);
    try expect(roundDownToPow2(8) == 8);
    try expect(roundDownToPow2(13) == 8);
    try expect(roundDownToPow2(200) == 128);
    try expect(roundDownToPow2(0xFFFFFFFF) == 0x80000000);
}

test "floorLog2" {
    try expect(floorLog2(1) == 0);
    try expect(floorLog2(2) == 1);
    try expect(floorLog2(3) == 1);
    try expect(floorLog2(8) == 3);
    try expect(floorLog2(15) == 3);
    try expect(floorLog2(16) == 4);
    try expect(floorLog2(200) == 7);
    try expect(floorLog2(0xFFFFFFFF) == 31);
}

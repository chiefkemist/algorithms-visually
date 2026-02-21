const std = @import("std");
const expect = std.testing.expect;

/// Branchless absolute value: y = x >> 31; (x ^ y) - y
pub fn branchlessAbs(x: i32) i32 {
    const y = x >> 31;
    return (x ^ y) -% y;
}

/// Branchless negative absolute value: y = x >> 31; y - (x ^ y)
pub fn branchlessNabs(x: i32) i32 {
    const y = x >> 31;
    return y -% (x ^ y);
}

test "branchlessAbs" {
    try expect(branchlessAbs(0) == 0);
    try expect(branchlessAbs(1) == 1);
    try expect(branchlessAbs(-1) == 1);
    try expect(branchlessAbs(42) == 42);
    try expect(branchlessAbs(-42) == 42);
    try expect(branchlessAbs(2147483647) == 2147483647);
    try expect(branchlessAbs(-2147483647) == 2147483647);
}

test "branchlessNabs" {
    try expect(branchlessNabs(0) == 0);
    try expect(branchlessNabs(1) == -1);
    try expect(branchlessNabs(-1) == -1);
    try expect(branchlessNabs(42) == -42);
    try expect(branchlessNabs(-42) == -42);
    try expect(branchlessNabs(2147483647) == -2147483647);
    try expect(branchlessNabs(-2147483647) == -2147483647);
    try expect(branchlessNabs(-2147483648) == -2147483648);
}

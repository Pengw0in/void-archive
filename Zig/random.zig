const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    // Use the default random number generator
    var prng = std.Random.DefaultPrng.init(blk: {
        var seed: u64 = undefined;
        std.posix.getrandom(std.mem.asBytes(&seed)) catch unreachable;
        break :blk seed;
    });

    const random = prng.random();

    const charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const charset_len = charset.len;

    var random_string: [5]u8 = undefined;

    for (&random_string) |*c| {
        const idx = random.intRangeLessThan(usize, 0, charset_len);
        c.* = charset[idx];
    }

    try stdout.print("Random String: {s}\n", .{random_string});
}
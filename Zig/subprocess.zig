const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    var process = std.process.Child.init(
        &.{ "rm", "/Users/lohithsrikar/Desktop/delete.txt" },
        std.heap.page_allocator,
    );

    process.stdout_behavior = .Pipe;

    try process.spawn();

    if (process.stdout) |out_stream| {
        var buffer: [1024]u8 = undefined;
        const reader = out_stream.reader();
        const bytes_read = try reader.readAll(&buffer);

        const output = buffer[0..bytes_read];
        try stdout.print("Captured output: {s}\n", .{output});
    }

    _ = try process.wait();
}

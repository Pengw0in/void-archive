const std = @import("std");

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    var map = std.StringHashMap(i32).init(allocator);

    defer map.deinit();

    try map.put("apple", 2);
    try map.put("banana", 6);
    try map.put("cherry", 8);
    try map.put("orange", 9);
    try map.put("jackfruit", 7);
    try map.put("jackfruit", 7);
    try map.put("jackfruit", 7);
    try map.put("jackfruit", 7);
    try map.put("jackfruit", 7);
    try map.put("jackfruit", 7);


    if (map.get("banana")) |value| {
        std.debug.print("banana = {}\n", .{value});
    } else {
        std.debug.print("banana not found\n", .{});
    }
    
    std.debug.print("capacity: {}\n", .{map.capacity()});
}
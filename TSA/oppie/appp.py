import curses
from curses import wrapper
import re

# Banner lines
BANNER_LINES = [
    " ________  ________  ________  ___  _______      ",
    "|\\   __  \\|\\   __  \\|\\   __  \\|\\  \\|\\  ___ \\     ",
    "\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\ \\   __/|    ",
    " \\ \\  \\\\\\  \\ \\   ____\\ \\   ____\\ \\  \\ \\  \\_|/__  ",
    "  \\ \\  \\\\\\  \\ \\  \\___|\\ \\  \\___|\\ \\  \\ \\  \\_|\\ \\ ",
    "   \\ \\_______\\ \\__\\    \\ \\__\\    \\ \\__\\ \\_______\\",
    "    \\|_______|\\|__|     \\|__|     \\|__|\\|_______|",
    "                                                 "
]

# Menu options
MENU_ITEMS = [
    "1. Start new session",
    "2. View history",
    "3. Settings",
    "4. Help",
    "5. Exit"
]

def fuzzy_match(pattern, text):
    """Simple fuzzy matching algorithm similar to FZF"""
    pattern = '.*?'.join(map(re.escape, pattern.lower()))
    return re.search(pattern, text.lower()) is not None

def draw_banner(stdscr, y_offset=1):
    """Draw the banner at the specified y_offset with magenta for first half, cyan for second half"""
    height, width = stdscr.getmaxyx()
    banner_width = len(BANNER_LINES[0])
    
    # Center the banner horizontally
    x_offset = max(0, (width - banner_width) // 2)
    
    # Display each line of the banner with color gradient
    # Divide the banner lines in half to apply different colors
    mid_point = len(BANNER_LINES) // 2
    
    for i, line in enumerate(BANNER_LINES):
        if y_offset + i >= height:  # Skip if line is beyond bottom of screen
            continue
            
        # Use color pair 1 (magenta) for first half, 2 (cyan) for second half
        color = 1 if i < mid_point else 2
        
        stdscr.attron(curses.color_pair(color))
        try:
            # Truncate the line if needed to fit within screen width
            display_line = line[:width-x_offset-1] if x_offset + len(line) >= width else line
            stdscr.addstr(y_offset + i, x_offset, display_line)
        except curses.error:
            pass  # Ignore if we go off-screen
        stdscr.attroff(curses.color_pair(color))
    
    return y_offset + len(BANNER_LINES)

def draw_menu_with_filter(stdscr, y_offset, items, selected=0, filter_text=""):
    """Draw the menu options with filtering support"""
    height, width = stdscr.getmaxyx()
    
    # Add some padding before menu
    y_offset += 2
    
    # Filter items based on input
    if filter_text:
        filtered_items = [item for item in items if fuzzy_match(filter_text, item)]
    else:
        filtered_items = items
    
    if not filtered_items:
        # Show "No matches" if no items match the filter
        no_match_msg = "No matches found"
        try:
            stdscr.addstr(y_offset, max(0, (width - len(no_match_msg)) // 2), no_match_msg)
        except curses.error:
            pass
        return y_offset + 1, filtered_items, 0
    
    # Adjust selected index if it's out of range for filtered items
    selected = min(selected, len(filtered_items) - 1)
    
    # Center menu items
    x_offset = max(0, (width - max(len(item) for item in filtered_items)) // 2)
    
    # Display menu items
    for i, item in enumerate(filtered_items):
        # Skip if this menu item would go below the screen
        if y_offset + i >= height:
            continue
            
        if i == selected:
            stdscr.attron(curses.A_REVERSE)
        try:
            stdscr.addstr(y_offset + i, x_offset, item)
        except curses.error:
            pass  # Ignore if we go off-screen
        if i == selected:
            stdscr.attroff(curses.A_REVERSE)
    
    # Return the end position and the filtered items
    return y_offset + len(filtered_items), filtered_items, selected

def main(stdscr):
    # Setup
    curses.curs_set(0)
    stdscr.clear()

    # Initialize colors more efficiently
    curses.start_color()
    curses.use_default_colors()
    
    # Reduce redundant color pairs
    curses.init_pair(1, curses.COLOR_MAGENTA, -1)  # Magenta for top half
    curses.init_pair(2, curses.COLOR_CYAN, -1)     # Cyan for bottom half

    # App state
    current_selection = 0
    filter_text = ""
    filter_mode = False
    full_redraw = True
    
    while True:
        if full_redraw:
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            # Fix: Correct box drawing - avoid writing to bottom-right corner which causes errors
            try:
                # Draw the border manually to avoid the bottom-right corner issue
                # Top and bottom borders
                for x in range(0, width-1):
                    stdscr.addch(0, x, curses.ACS_HLINE)
                    stdscr.addch(height-1, x, curses.ACS_HLINE)
                
                # Left and right borders
                for y in range(0, height-1):
                    stdscr.addch(y, 0, curses.ACS_VLINE)
                    stdscr.addch(y, width-1, curses.ACS_VLINE)
                
                # Corners
                stdscr.addch(0, 0, curses.ACS_ULCORNER)
                stdscr.addch(0, width-1, curses.ACS_URCORNER)
                stdscr.addch(height-1, 0, curses.ACS_LLCORNER)
                # Don't draw the bottom-right corner to avoid errors
                if height > 1 and width > 1:
                    stdscr.addch(height-1, width-1, curses.ACS_LRCORNER)
            except curses.error:
                pass
                
            # Draw title
            title = "OPPIE - Terminal Audio Player"
            try:
                stdscr.addstr(0, max(1, min(width-2, (width - len(title)) // 2)),
                             title[:width-3] if len(title) > width-3 else title)
            except curses.error:
                pass
                
            # Draw banner and static elements
            banner_end_y = draw_banner(stdscr, 3)
            
            # Draw version info
            version = "v1.0.0"
            try:
                if width > len(version) + 3:  # Make sure we have room + buffer
                    pos_x = min(width - len(version) - 3, width - 2)
                    stdscr.addstr(height-1, pos_x, version)
            except curses.error:
                pass
                
            full_redraw = False
        
        # Clear the menu area before redrawing
        for y in range(banner_end_y, height-2):
            try:
                stdscr.move(y, 1)
                stdscr.clrtoeol()
            except curses.error:
                pass
        
        # Draw filter input if in filter mode
        if filter_mode:
            filter_prompt = "Filter: " + filter_text + "█"  # Add cursor
            try:
                stdscr.addstr(banner_end_y + 2, max(0, (width - len(filter_prompt)) // 2), filter_prompt)
            except curses.error:
                pass
            menu_start_y = banner_end_y + 4
        else:
            menu_start_y = banner_end_y
        
        # Draw menu with filtering
        menu_end_y, filtered_items, current_selection = draw_menu_with_filter(
            stdscr, menu_start_y, MENU_ITEMS, current_selection, filter_text)
        
        # Add footer only if there's room
        footer = "↑/↓: Navigate | Enter: Select | /: Search | Esc: Exit" 
        if menu_end_y + 2 < height:
            try:
                stdscr.addstr(menu_end_y + 2, max(0, (width - len(footer)) // 2), footer)
            except curses.error:
                pass
        
        # Update screen
        stdscr.refresh()

        # Handle input
        key = stdscr.getch()

        if filter_mode:
            # Handle filter mode input
            if key == 27:  # ESC key - exit filter mode
                filter_mode = False
                filter_text = ""
                full_redraw = True
            elif key == 10 or key == 13:  # Enter - select current item and exit filter mode
                filter_mode = False
                if filtered_items:  # Only if we have filtered items
                    # Find the index of the selected filtered item in the original list
                    selected_item = filtered_items[current_selection]
                    current_selection = MENU_ITEMS.index(selected_item)
            elif key == 8 or key == 127:  # Backspace
                if filter_text:
                    filter_text = filter_text[:-1]
            elif 32 <= key <= 126:  # Printable characters
                filter_text += chr(key)
            elif key == curses.KEY_UP:
                current_selection = max(0, current_selection - 1)
            elif key == curses.KEY_DOWN:
                current_selection = min(len(filtered_items) - 1, current_selection + 1) if filtered_items else 0
        else:
            # Regular navigation mode
            if key == curses.KEY_UP:
                current_selection = max(0, current_selection - 1)
            elif key == curses.KEY_DOWN:
                current_selection = min(len(MENU_ITEMS) - 1, current_selection + 1)
            elif key == ord('/'):  # Forward slash key to enter filter mode
                filter_mode = True
                filter_text = ""
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_selection == len(MENU_ITEMS) - 1:  # Exit option
                    break
                
                # Show selected option in middle of screen
                stdscr.clear()
                stdscr.box()
                message = f"You selected: {MENU_ITEMS[current_selection]}"
                stdscr.addstr(height//2, (width - len(message))//2, message)
                stdscr.addstr(height//2 + 2, (width - 30)//2, "Press any key to return...")
                stdscr.refresh()
                stdscr.getch()
                full_redraw = True
            elif key == 27:  # ESC key
                break

if __name__ == "__main__":
    wrapper(main)
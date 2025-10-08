import curses

def main(stdscr):
    # Setup
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    
    # Initialize color functionality
    curses.start_color()
    curses.use_default_colors()  # This enables -1 as a color value
    
    # Initialize color pairs
    try:
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # White text
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Cyan text
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Yellow text
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)# Magenta text
        curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)    # Red text
        curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLACK)   # Blue text
    except curses.error:
        # Fallback if color pairs don't work
        pass

    stdscr.clear()

    try:
        # Example usage of color pairs
        stdscr.addstr(0, 0, "Elegant and Professional: ", curses.color_pair(1))
        stdscr.addstr("This is White and Cyan\n", curses.color_pair(2))

        stdscr.addstr(1, 0, "Vibrant and Fun: ", curses.color_pair(1))
        stdscr.addstr("This is Yellow and Magenta\n", curses.color_pair(4))

        stdscr.addstr(2, 0, "Calm and Soft: ", curses.color_pair(1))
        stdscr.addstr("This is Green and Blue\n", curses.color_pair(7))

        stdscr.addstr(3, 0, "Bold and Clear: ", curses.color_pair(1))
        stdscr.addstr("This is Red and White\n", curses.color_pair(6))

        stdscr.addstr(4, 0, "Subtle but Modern: ", curses.color_pair(1))
        stdscr.addstr("This is Cyan and Green\n", curses.color_pair(5))
    except curses.error:
        # Handle potential positioning errors
        height, width = stdscr.getmaxyx()
        stdscr.addstr(0, 0, f"Terminal too small ({width}x{height}). Please resize.")
    
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

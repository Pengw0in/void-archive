from rich.console import Console
from rich.text import Text

console = Console()

banner_lines = [
    " ________  ________  ________  ___  _______      ",
    "|\\   __  \\|\\   __  \\|\\   __  \\|\\  \\|\\  ___ \\     ",
    "\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\ \\   __/|    ",
    " \\ \\  \\\\\\  \\ \\   ____\\ \\   ____\\ \\  \\ \\  \\_|/__  ",
    "  \\ \\  \\\\\\  \\ \\  \\___|\\ \\  \\___|\\ \\  \\ \\  \\_|\\ \\ ",
    "   \\ \\_______\\ \\__\\    \\ \\__\\    \\ \\__\\ \\_______\\",
    "    \\|_______|\\|__|     \\|__|     \\|__|\\|_______|",
    "                                                 "
]

# Gradient colors from yellow to blue
gradient_colors = [
   "#2A0A5C", "#4B2A89", "#7C55B4", "#AD7FDF",
    "#D6A4F0", "#F0BCE9", "#FBCFE8", "#FFDDEE"
]

for line, color in zip(banner_lines, gradient_colors):
    text = Text(line, style=color)
    console.print(text)

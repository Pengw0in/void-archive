from colorama import init, Fore, Style
import curses

init(autoreset=True)

banner_lines = [
    f"{Fore.BLUE}{Style.BRIGHT} ________  ________  ________  ________  ___  _______      {Style.RESET_ALL}",
    f"{Fore.BLUE}{Style.BRIGHT}|\\   __  \\|\\   __  \\|\\   __  \\|\\   __  \\|\\  \\|\\  ___ \\     {Style.RESET_ALL}{Fore.RED}{Style.NORMAL}♬{Style.RESET_ALL}",
    f"{Fore.BLUE}{Style.BRIGHT}\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\ \\   __/|    {Style.RESET_ALL}{Fore.YELLOW}{Style.BRIGHT}              ♫{Style.RESET_ALL}",
    f"{Fore.BLUE}{Style.NORMAL} \\ \\  \\\\\\  \\ \\   ____\\ \\   ____\\ \\   ____\\ \\  \\ \\  \\_|/__  {Style.RESET_ALL}{Fore.MAGENTA}{Style.BRIGHT}     ╱|、{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.NORMAL}  \\ \\  \\\\\\  \\ \\  \\___|\\  \\___|\\  \\___| \\  \\ \\  \\_|\\ \\ {Style.RESET_ALL}{Fore.MAGENTA}{Style.BRIGHT}    (`. - 7{Style.RESET_ALL}{Fore.CYAN}{Style.BRIGHT} ♪{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.NORMAL}   \ \_______\ \__\    \ \__\    \ \__\    \ \__\ \_______\{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}   {Style.RESET_ALL}{Fore.MAGENTA}{Style.BRIGHT}|、  〵{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.DIM}    \\|_______|\\|__|     \\|__|     \\|__|     \\|__|\\|_______|{Style.RESET_ALL}{Fore.CYAN}{Style.NORMAL} meow{Style.RESET_ALL}{Fore.MAGENTA}{Style.BRIGHT}じしˍ,)ノ{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.DIM}                                                           {Style.RESET_ALL}"
]

print("\n".join(banner_lines))
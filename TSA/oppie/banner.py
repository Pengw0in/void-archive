from colorama import init, Fore, Style

init(autoreset=True)

banner_lines = [
    f"{Fore.BLUE}{Style.BRIGHT} _______  _______  _______  ___   _______ {Style.RESET_ALL}    ",
    f"{Fore.BLUE}{Style.BRIGHT}|       ||       ||       ||   | |       |{Style.RESET_ALL}    {Fore.BLUE}{Style.BRIGHT}   ♬{Style.RESET_ALL}",
    f"{Fore.BLUE}{Style.BRIGHT}|   _   ||    _  ||    _  ||   | |    ___|{Style.RESET_ALL}    {Fore.YELLOW}{Style.BRIGHT}                              ♫{Style.RESET_ALL}",
    f"{Fore.BLUE}{Style.NORMAL}|  | |  ||   |_| ||   |_| ||   | |   |___ {Style.RESET_ALL}       {Fore.WHITE}{Style.NORMAL}      ▄▀▄     ▄▀▄{Style.RESET_ALL}{Fore.MAGENTA}{Style.BRIGHT}     ♪{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.NORMAL}|  |_|  ||    ___||    ___||   | |    ___|{Style.RESET_ALL}       {Fore.WHITE}{Style.DIM}     ▄█░░▀▀▀▀▀░░█▄{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.NORMAL}|       ||   |    |   |    |   | |   |___ {Style.RESET_ALL}   {Fore.YELLOW}{Style.BRIGHT}  ♪ {Style.RESET_ALL}{Fore.WHITE}{Style.BRIGHT} ▄▄{Style.RESET_ALL}{Fore.BLACK}{Style.BRIGHT}  █░░░░░░░░░░░█  {Style.RESET_ALL}{Fore.WHITE}{Style.BRIGHT}▄▄ {Style.RESET_ALL}"  , 
    f"{Fore.YELLOW}{Style.DIM}|_______||___|    |___|    |___| |_______|{Style.RESET_ALL}       {Fore.BLACK}{Style.BRIGHT}█▄▄█ █░░{Fore.WHITE}{Style.BRIGHT}▀{Style.RESET_ALL}░░┬░░{Fore.WHITE}{Style.BRIGHT}▀{Style.RESET_ALL}{Fore.BLACK}{Style.BRIGHT}░░█ █▄▄█{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.DIM}    {Style.RESET_ALL}                                              {Fore.BLACK}{Style.BRIGHT}     {Style.RESET_ALL}"
]

print("\n".join(banner_lines))



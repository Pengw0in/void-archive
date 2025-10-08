from search import yt_dlp_search
from select_fzf import select_result

results = yt_dlp_search("suzume")
choice = select_result(results)

if choice:
    print(choice)
else:
    print("ahhh")

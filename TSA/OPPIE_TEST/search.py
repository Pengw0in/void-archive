import os
import subprocess
from utils import load_cache, save_cache, is_cache_valid

def yt_dlp_fetch(query: str) -> list:
    cmd = [
        "yt-dlp",
        f"ytsearch5:{query}",
        "--flat-playlist",
        "--print", "%(title)s (%(duration_string)s) | %(webpage_url)s",
        "--skip-download",
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split("\n")
    return [line for line in lines if line.strip()]

def yt_dlp_search(query: str) -> list:
    cache = load_cache()

    if query in cache and is_cache_valid(cache[query]['time']):
        return cache[query]['results'] 

    results = yt_dlp_fetch(query)

    if results:
        cache[query] = {
            'time': datetime.now().timestamp(),
            'results' : results
        }
        save_cache(cache)

    return results



import subprocess
import json
import sys
import os
import pickle
from datetime import datetime, timedelta

# Cache directory and file
CACHE_DIR = os.path.expanduser("~/.cache/yt_search_fzf")
CACHE_FILE = os.path.join(CACHE_DIR, "search_cache.pkl")
CACHE_EXPIRY = 24 * 60 * 60  # Cache expires after 24 hours

def load_cache():
    """Load the search cache from disk"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache):
    """Save the search cache to disk"""
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)

def search_youtube(query):
    """Search YouTube with caching support"""
    cache = load_cache()
    current_time = datetime.now().timestamp()
    
    # Check if we have a cached result that's still valid
    if query in cache and (current_time - cache[query]['time'] < CACHE_EXPIRY):
        return cache[query]['results']
    
    # No valid cache - perform the search
    command = [
        "yt-dlp",
        f"ytsearch10:{query}",
        "--print", "%(title)s (%(duration_string)s) | %(webpage_url)s",
        "--no-warnings",
        "--skip-download",
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    results = result.stdout.strip().split("\n")
    
    # Cache the results
    if results and results[0]:  # Only cache if we got results
        cache[query] = {
            'time': current_time,
            'results': results
        }
        save_cache(cache)
    
    return results

def pick_with_fzf(options):
    fzf = subprocess.run(["fzf", "--prompt", "Select video: "], input="\n".join(options), capture_output=True, text=True)
    return fzf.stdout.strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python yt_search_fzf.py <search keyword>")
        sys.exit(1)

    keyword = " ".join(sys.argv[1:])
    print("Searching YouTube...")
    results = search_youtube(keyword)

    if not results or not results[0]:
        print("No results found.")
        return

    choice = pick_with_fzf(results)
    if choice:
        print(f"\nYou selected:\n{choice}")
    else:
        print("No selection made.")

if __name__ == "__main__":
    main()

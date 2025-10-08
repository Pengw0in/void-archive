import os
import pickle
from datetime import datetime, timedelta

CACHE_DIR = os.path.expanduser("~/.cache/search_oppie")
CACHE_FILE = os.path.join(CACHE_DIR, "search_cache.pkl")
CACHE_EXPIRY_SECONDS = 24 * 60 * 60

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, 'rb') as fl:
            return pickle.load(fl)
    except Exception:
        return {}

def save_cache(cache):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(CACHE_FILE, 'wb') as fl:
        pickle.dump(cache, fl)

def is_cache_valid(entry_timestamp: float) -> bool:
    return (datetime.now().timestamp() - entry_timestamp) < CACHE_EXPIRY_SECONDS
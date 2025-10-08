import re
import requests
from bs4 import BeautifulSoup
from youtube_comment_downloader import YoutubeCommentDownloader
from concurrent.futures import ThreadPoolExecutor, as_completed

downloader = YoutubeCommentDownloader()
flag_pattern = re.compile(r'FLAG\{.*?\}')

def extract_youtube_urls(page_url):
    try:
        r = requests.get(page_url, timeout=10)
        r.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(r.text, 'html.parser')
        links = set()
        for a in soup.find_all('a', href=True):
            href = a['href']
            if 'youtube.com/watch?v=' in href or 'youtu.be/' in href:
                if href.startswith('/watch'):
                    href = 'https://www.youtube.com' + href
                links.add(href)
        return list(links)
    except requests.RequestException as e:
        print(f"[!] Error fetching page: {e}")
        return []

def search_comments(url):
    flags = []
    print(f"[*] Scanning comments for: {url}")
    try:
        comment_count = 0
        comments = downloader.get_comments_from_url(url)
        for comment in comments:
            comment_count += 1
            if comment_count % 100 == 0:  # Log progress every 100 comments
                print(f"    → Processed {comment_count} comments for {url}")
                
            if isinstance(comment, dict) and 'text' in comment:
                matches = flag_pattern.findall(comment['text'])
                if matches:
                    flags.extend(matches)
                    if flags:
                        print(f"    ✓ Found flag after scanning {comment_count} comments")
                        break
        print(f"[+] Finished scanning {comment_count} comments for: {url}")
    except Exception as e:
        print(f"[!] Error: {url} -> {e}")
    return url, flags

# === Main ===
page_url = 'https://aictf.phdays.fun/files/flagleak_d3eec25.html'
urls = extract_youtube_urls(page_url)
print(f"[+] Found {len(urls)} video URLs to scan")
print("-" * 50)

completed = 0
with ThreadPoolExecutor(max_workers=16) as executor:
    future_to_url = {executor.submit(search_comments, url): url for url in urls}
    for future in as_completed(future_to_url):
        completed += 1
        url, flags = future.result()
        if flags:
            print(f"\n[!] FLAG FOUND in video {completed}/{len(urls)}: {url}")
            for f in flags:
                print(f"    {f}")
        print(f"[*] Progress: {completed}/{len(urls)} videos processed")
        print("-" * 50)

#!/usr/bin/env python3

import json
import logging
import random
import re
import requests
import subprocess
import sys
import time
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("AnimeStreamFetcher")

# Constants
ANIMEPAHE_BASE = "https://animepahe.ru"
ANIMEPAHE_ENDPOINT = f"{ANIMEPAHE_BASE}/api"
# Fix the regex to avoid variable-width lookbehind
JUICY_STREAM_REGEX = re.compile(r'const\s+\w+\s*=\s*["\']([^"\']+)["\']|source\s*=\s*["\']([^"\']+)["\']')

# Headers to mimic browser request
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0"
]

# Request headers
REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "DNT": "1",
}

# Server headers with proper referer
SERVER_HEADERS = {
    "Host": "kwik.si",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": f"{ANIMEPAHE_BASE}/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
}

class ProviderStore:
    """Simple in-memory store for anime data"""
    def __init__(self):
        self.store = {}
    
    def set(self, key: str, namespace: str, value: any):
        if key not in self.store:
            self.store[key] = {}
        self.store[key][namespace] = value
    
    def get(self, key: str, namespace: str) -> Optional[any]:
        return self.store.get(key, {}).get(namespace)


def get_random_user_agent() -> str:
    """Get a random user agent from the list"""
    return random.choice(USER_AGENTS)


def get_element_by_id(element_id: str, html_content: str) -> str:
    """Extract an element by its ID from HTML content"""
    pattern = rf'<[^>]*\bid=["\']?{element_id}["\']?[^>]*>(.*?)</[^>]*>'
    match = re.search(pattern, html_content, re.DOTALL)
    return match.group(0) if match else ""


def get_elements_html_by_class(class_name: str, html_content: str) -> List[str]:
    """Extract elements by class name from HTML content"""
    pattern = rf'<[^>]*\bclass=["\']?[^"\']*\b{class_name}\b[^"\']*["\']?[^>]*>.*?</[^>]*>'
    return re.findall(pattern, html_content, re.DOTALL)


def extract_attributes(html_element: str) -> Dict[str, str]:
    """Extract attributes from HTML element"""
    result = {}
    
    # Extract data-src attribute
    data_src_match = re.search(r'data-src=["\']([^"\']*)["\']', html_element)
    if data_src_match:
        result["data-src"] = data_src_match.group(1)
    
    # Extract data-audio attribute
    data_audio_match = re.search(r'data-audio=["\']([^"\']*)["\']', html_element)
    if data_audio_match:
        result["data-audio"] = data_audio_match.group(1)
    
    # Extract data-resolution attribute
    data_resolution_match = re.search(r'data-resolution=["\']([^"\']*)["\']', html_element)
    if data_resolution_match:
        result["data-resolution"] = data_resolution_match.group(1)
    
    return result


def process_animepahe_embed_page(html_content: str) -> Optional[str]:
    """Extract and decode JavaScript from the kwik embed page"""
    try:
        # Extract the obfuscated JavaScript
        kwik_js_match = re.search(r'eval\((function\(p,a,c,k,e,.*?)\)\)', html_content, re.DOTALL)
        if not kwik_js_match:
            logger.error("Failed to find obfuscated JavaScript")
            return None
        
        # Use regex to search directly for source URL
        # This is simpler than trying to deobfuscate JavaScript in Python
        source_match = re.search(r'source[=:]\s*[\'"](https?://[^\'"]+)[\'"]', html_content)
        if source_match:
            return f"const source = '{source_match.group(1)}'"
            
        # If we didn't find it directly, try another approach with the obfuscated code
        obfuscated_code = kwik_js_match.group(0)
        source_match = re.search(r'source[=:]\s*[\'"](https?://[^\'"]+)[\'"]', obfuscated_code)
        if source_match:
            return f"const source = '{source_match.group(1)}'"
            
        return kwik_js_match.group(1) + "()"
    except Exception as e:
        logger.error(f"Error processing embed page: {e}")
        return None


class AnimePaheFetcher:
    """Fetch anime streams from AnimePahe with anti-automation measures"""
    
    def __init__(self):
        self.session = requests.Session()
        self.user_agent = get_random_user_agent()
        self.session.headers.update({"User-Agent": self.user_agent, **REQUEST_HEADERS})
        self.store = ProviderStore()
        
        # Add a small delay to mimic human behavior
        time.sleep(random.uniform(0.5, 1.5))
    
    def _throttled_request(self, method: str, url: str, **kwargs):
        """Make a throttled request to avoid rate limiting"""
        # Randomized delay between requests
        time.sleep(random.uniform(0.2, 1.0))
        
        # Add jitter to headers occasionally to appear more human-like
        if random.random() < 0.3:
            if "headers" not in kwargs:
                kwargs["headers"] = {}
            
            # Sometimes change user agent
            if random.random() < 0.5:
                kwargs["headers"]["User-Agent"] = get_random_user_agent()
                
            # Sometimes add or modify accept header
            if random.random() < 0.3:
                accept_values = [
                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ]
                kwargs["headers"]["Accept"] = random.choice(accept_values)
        
        # Make the request
        response = getattr(self.session, method)(url, **kwargs)
        
        # Handle response based on status code
        if response.status_code == 429:  # Too Many Requests
            retry_after = int(response.headers.get('Retry-After', 5))
            logger.warning(f"Rate limited. Waiting {retry_after} seconds")
            time.sleep(retry_after + random.uniform(0.5, 2.0))
            return self._throttled_request(method, url, **kwargs)
            
        response.raise_for_status()
        return response
    
    def search_for_anime(self, search_keywords: str):
        """Search for anime by keywords"""
        logger.info(f"Searching for '{search_keywords}'")
        
        # Use throttled request
        response = self._throttled_request(
            "get", 
            ANIMEPAHE_ENDPOINT, 
            params={"m": "search", "q": search_keywords}
        )
        
        data = response.json()
        results = []
        
        for result in data["data"]:
            results.append({
                "availableEpisodes": list(range(result["episodes"])),
                "id": result["session"],
                "title": result["title"],
                "type": result["type"],
                "year": result["year"],
                "score": result["score"],
                "status": result["status"],
                "season": result["season"],
                "poster": result["poster"],
            })
            # Store result for later use
            self.store.set(str(result["session"]), "search_result", result)
        
        return {
            "pageInfo": {
                "total": data["total"],
                "perPage": data["per_page"],
                "currentPage": data["current_page"],
            },
            "results": results,
        }
    
    def _pages_loader(self, data, session_id, params, page):
        """Load multiple pages of results with throttling"""
        response = self._throttled_request("get", ANIMEPAHE_ENDPOINT, params=params)
        
        if not data:
            data.update(response.json())
        else:
            if ep_data := response.json().get("data"):
                data["data"].extend(ep_data)
                
        # If there are more pages, recursively load them with throttling
        if response.json()["next_page_url"]:
            # Add random delay between page loads
            time.sleep(random.uniform(0.5, 2.0))
            page += 1
            self._pages_loader(
                data,
                session_id,
                params={
                    "m": "release",
                    "page": page,
                    "id": session_id,
                    "sort": "episode_asc",
                },
                page=page,
            )
        return data
    
    def get_anime(self, session_id: str):
        """Get anime details by session ID"""
        page = 1
        if d := self.store.get(str(session_id), "search_result"):
            anime_result = d
            data = {}
            
            data = self._pages_loader(
                data,
                session_id,
                params={
                    "m": "release",
                    "id": session_id,
                    "sort": "episode_asc",
                    "page": page,
                },
                page=page,
            )
            
            if not data:
                return {}
                
            data["title"] = anime_result["title"]
            self.store.set(str(session_id), "anime_info", data)
            episodes = list(map(str, [episode["episode"] for episode in data["data"]]))
            title = ""
            
            return {
                "id": session_id,
                "title": anime_result["title"],
                "year": anime_result["year"],
                "season": anime_result["season"],
                "poster": anime_result["poster"],
                "score": anime_result["score"],
                "availableEpisodesDetail": {
                    "sub": episodes,
                    "dub": episodes,
                    "raw": episodes,
                },
                "episodesInfo": [
                    {
                        "title": f"{episode['title'] or title};{episode['episode']}",
                        "episode": episode["episode"],
                        "id": episode["session"],
                        "translation_type": episode["audio"],
                        "duration": episode["duration"],
                        "poster": episode["snapshot"],
                    }
                    for episode in data["data"]
                ],
            }
    
    def _get_server(self, episode, res_dicts, anime_title, translation_type):
        """Extract streaming links from servers"""
        streams = {
            "server": "kwik",
            "links": [],
            "episode_title": f"{episode['title'] or anime_title}; Episode {episode['episode']}",
            "subtitles": [],
            "headers": {},
        }
        
        for res_dict in res_dicts:
            # Get embed URL
            embed_url = res_dict["data-src"]
            data_audio = "dub" if res_dict["data-audio"] == "eng" else "sub"
            
            # Filter streams by translation type
            if data_audio != translation_type:
                continue
            
            if not embed_url:
                logger.warning("Embed URL not found")
                continue
                
            # Get embed page with anti-detection measures
            embed_response = self._throttled_request(
                "get",
                embed_url, 
                headers={
                    "User-Agent": self.user_agent, 
                    **SERVER_HEADERS,
                    "Referer": f"{ANIMEPAHE_BASE}/",
                    "Sec-Fetch-Dest": "iframe",
                }
            )
            
            embed_page = embed_response.text
            
            # Process the JavaScript to extract stream URL
            decoded_js = process_animepahe_embed_page(embed_page)
            if not decoded_js:
                logger.error("Failed to decode embed page")
                continue
                
            juicy_stream = JUICY_STREAM_REGEX.search(decoded_js)
            if not juicy_stream:
                logger.error("Failed to find stream URL")
                continue
                
            # Get the first non-None group from the match
            juicy_stream = next((g for g in juicy_stream.groups() if g is not None), None)
            if not juicy_stream:
                logger.error("Failed to extract stream URL")
                continue
            
            # Add the link to results
            streams["links"].append({
                "quality": res_dict["data-resolution"],
                "translation_type": data_audio,
                "link": juicy_stream,
            })
            
        return streams
    
    def get_episode_streams(self, anime_id, episode_number, translation_type):
        """Get streaming links for a specific episode"""
        # Get anime info from store
        anime_info = self.store.get(str(anime_id), "anime_info")
        if not anime_info:
            logger.error(f"Anime with ID {anime_id} not found in store")
            return None
            
        anime_title = anime_info["title"]
        
        # Find the episode in the anime info
        episode = next(
            (ep for ep in anime_info["data"] if float(ep["episode"]) == float(episode_number)),
            None,
        )
        
        if not episode:
            logger.error(f"Episode {episode_number} doesn't exist for anime {anime_title}")
            return None
            
        # Fetch the episode page
        url = f"{ANIMEPAHE_BASE}/play/{anime_id}/{episode['session']}"
        response = self._throttled_request("get", url)
        
        # Extract streaming options
        c = get_element_by_id("resolutionMenu", response.text)
        resolutionMenuItems = get_elements_html_by_class("dropdown-item", c)
        res_dicts = [extract_attributes(item) for item in resolutionMenuItems]
        
        if _server := self._get_server(episode, res_dicts, anime_title, translation_type):
            return _server
        return None


def print_with_color(text, color):
    """Print colored text in terminal"""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['end']}")


def main():
    """Main function to run the script"""
    try:
        print_with_color("\n=== AnimePahe Stream Fetcher ===", "cyan")
        fetcher = AnimePaheFetcher()
        
        # Step 1: Search for anime
        search_term = input("\nEnter anime name: ")
        print_with_color(f"\nSearching for '{search_term}'...", "blue")
        
        search_results = fetcher.search_for_anime(search_term)
        
        if not search_results or not search_results["results"]:
            print_with_color("No results found.", "red")
            return
            
        # Step 2: Display search results
        print_with_color("\nSearch Results:", "green")
        for idx, result in enumerate(search_results["results"], start=1):
            print(f"{idx}. {result['title']} ({result['year']}) - Score: {result['score']}")
            
        # Step 3: Select anime
        choice = int(input("\nSelect anime number: ")) - 1
        if choice < 0 or choice >= len(search_results["results"]):
            print_with_color("Invalid selection.", "red")
            return
            
        anime_id = search_results["results"][choice]["id"]
        
        # Step 4: Get anime details with progress indicator
        print_with_color("\nFetching anime details...", "blue")
        anime_details = fetcher.get_anime(anime_id)
        
        if not anime_details:
            print_with_color("Failed to get anime details.", "red")
            return
            
        print_with_color(f"\nSelected: {anime_details['title']}", "magenta")
        
        # Step 5: Select translation type
        print_with_color("\nAvailable Translation Types:", "green")
        translation_types = ["sub", "dub"]
        for idx, trans_type in enumerate(translation_types, start=1):
            print(f"{idx}. {trans_type.upper()}")
            
        trans_choice = int(input("\nSelect translation type: ")) - 1
        if trans_choice < 0 or trans_choice >= len(translation_types):
            print_with_color("Invalid selection.", "red")
            return
            
        translation_type = translation_types[trans_choice]
        
        # Step 6: List and select episode
        print_with_color("\nAvailable Episodes:", "green")
        episodes = sorted(
            anime_details["availableEpisodesDetail"][translation_type], 
            key=float
        )
        
        # Display episodes in a nice grid
        cols = 5
        for i in range(0, len(episodes), cols):
            row_episodes = episodes[i:i+cols]
            print(" ".join([f"{int(float(ep)):3d}" for ep in row_episodes]))
            
        ep_number = input("\nEnter episode number: ")
        
        # Step 7: Get stream links
        print_with_color(f"\nFetching stream for Episode {ep_number}...", "blue")
        stream_data = fetcher.get_episode_streams(anime_id, ep_number, translation_type)
        
        if not stream_data or not stream_data["links"]:
            print_with_color("No streams available.", "red")
            return
            
        # Step 8: Display stream qualities and select one
        print_with_color("\nAvailable Qualities:", "green")
        for idx, link in enumerate(stream_data["links"], start=1):
            print(f"{idx}. {link['quality']}")
            
        qual_choice = int(input("\nSelect quality (0 for all): "))
        
        if qual_choice == 0:
            # Display all stream URLs
            print_with_color("\nAll Stream URLs:", "yellow")
            for link in stream_data["links"]:
                print(f"{link['quality']}: {link['link']}")
        elif 1 <= qual_choice <= len(stream_data["links"]):
            # Display selected stream URL
            selected_link = stream_data["links"][qual_choice-1]
            print_with_color("\nSelected Stream URL:", "yellow")
            print(f"Quality: {selected_link['quality']}")
            print(f"URL: {selected_link['link']}")
            
            # Offer to play with MPV
            if input("\nPlay with MPV? (y/n): ").lower() == 'y':
                print_with_color("\nLaunching MPV player...", "blue")
                subprocess.run(["mpv", selected_link["link"]])
        else:
            print_with_color("Invalid selection.", "red")
            
    except KeyboardInterrupt:
        print_with_color("\nOperation cancelled by user.", "yellow")
    except Exception as e:
        print_with_color(f"\nError: {e}", "red")
        logging.error(f"Exception: {e}", exc_info=True)


if __name__ == "__main__":
    main()
import requests
import sys
import json

def get_anime_id(anime_name):
    """Search for an anime and return its ID"""
    search_url = f"
    "
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        results = response.json().get("results", [])
        
        if not results:
            print(f"No anime found with name: {anime_name}")
            sys.exit(1)
            
        # Return the first match ID
        return results[0]["id"]
    except requests.exceptions.RequestException as e:
        print(f"Error searching for anime: {e}")
        sys.exit(1)

def get_episode_id(anime_id, ep_num):
    """Get the specific episode ID from anime info"""
    info_url = f"https://api.consumet.org/anime/gogoanime/info/{anime_id}"
    try:
        response = requests.get(info_url)
        response.raise_for_status()
        anime_info = response.json()
        
        episodes = anime_info.get("episodes", [])
        
        # Find the requested episode
        for episode in episodes:
            if episode.get("number") == int(ep_num):
                return episode.get("id")
                
        print(f"Episode {ep_num} not found for {anime_id}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error getting anime info: {e}")
        sys.exit(1)

def get_streaming_links(episode_id):
    """Get streaming links for a specific episode"""
    stream_url = f"https://api.consumet.org/anime/gogoanime/watch/{episode_id}"
    try:
        response = requests.get(stream_url)
        response.raise_for_status()
        streaming_data = response.json()
        
        sources = streaming_data.get("sources", [])
        if not sources:
            print("No streaming sources found")
            return None
        
        # Create a dictionary of quality: url
        quality_links = {}
        for source in sources:
            quality_links[source.get("quality")] = source.get("url")
            
        return {
            "streams": quality_links,
            "download": streaming_data.get("download")
        }
    except requests.exceptions.RequestException as e:
        print(f"Error getting streaming links: {e}")
        return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python get_stream.py 'anime_name' episode_number")
        sys.exit(1)
        
    anime_name = sys.argv[1]
    ep_num = sys.argv[2]
    
    print(f"Searching for {anime_name}, episode {ep_num}...")
    
    # Step 1: Get anime ID from search
    anime_id = get_anime_id(anime_name)
    print(f"Found anime ID: {anime_id}")
    
    # Step 2: Get episode ID
    episode_id = get_episode_id(anime_id, ep_num)
    print(f"Found episode ID: {episode_id}")
    
    # Step 3: Get streaming links
    streaming_links = get_streaming_links(episode_id)
    
    if streaming_links:
        print("\n=== Streaming Links ===")
        for quality, url in streaming_links["streams"].items():
            print(f"\n{quality}: {url}")
        
        print("\n=== Download Link (secondary) ===")
        print(streaming_links["download"])
        
        # Save to a file for easy access
        with open(f"{anime_id}_ep{ep_num}_links.json", "w") as f:
            json.dump(streaming_links, f, indent=2)
        print(f"\nLinks saved to {anime_id}_ep{ep_num}_links.json")

if __name__ == "__main__":
    main()
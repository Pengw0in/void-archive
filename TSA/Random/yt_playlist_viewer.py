#!/usr/bin/env python3
"""
YouTube Playlist Viewer
-----------------------
A tool for browsing YouTube playlists and watching videos with MPV.
Uses yt-dlp for fetching video data and mpv for playback.

Requirements:
- yt-dlp (pip install yt-dlp)
- mpv (install via package manager)
Advanced Usage:
- For direct channel playlists: username:playlistname
  Example: TheCherno:C++
- URLs: Full YouTube playlist URLs
- Search: Any search term to find playlists
"""

import subprocess
import os
import sys
import json
import argparse
import shutil
from urllib.parse import urlparse, parse_qs

# Check for required dependencies
def check_dependencies():
    dependencies = {
        "yt-dlp": shutil.which("yt-dlp"),
        "mpv": shutil.which("mpv")
    }
    
    missing = [dep for dep, path in dependencies.items() if not path]
    
    if missing:
        print("Error: Missing required dependencies:")
        for dep in missing:
            if dep == "yt-dlp":
                print(f"  - {dep}: Install with 'pip install yt-dlp'")
            else:
                print(f"  - {dep}: Install with your package manager")
        sys.exit(1)

# Get playlist ID from URL or search term
def get_playlist_id(query):
    # Check if query is a URL
    if "youtube.com" in query or "youtu.be" in query:
        parsed_url = urlparse(query)
        
        # For playlist URLs
        if "playlist" in query:
            query_params = parse_qs(parsed_url.query)
            if "list" in query_params:
                return query_params["list"][0]
        
        # For video in playlist URLs
        query_params = parse_qs(parsed_url.query)
        if "list" in query_params:
            return query_params["list"][0]
            
        print("Could not extract playlist ID from URL")
        return None
        
    # Try direct search for channel with specific playlist
    if ":" in query and " " not in query.split(":")[0]:
        # Format like "channel:playlist" to directly get a specific user's playlist
        parts = query.split(":", 1)
        channel = parts[0]
        playlist_query = parts[1]
        
        print(f"Searching for '{playlist_query}' playlists by {channel}")
        cmd = ["yt-dlp", "--flat-playlist", "--dump-json", "--no-warnings", 
               f"https://www.youtube.com/@{channel}/playlists"]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            playlists = []
            
            for line in result.stdout.strip().split('\n'):
                if not line.strip():
                    continue
                try:
                    video_data = json.loads(line)
                    if 'title' in video_data and playlist_query.lower() in video_data.get('title', '').lower():
                        url = video_data.get('webpage_url', '')
                        url_parts = urlparse(url)
                        query_params = parse_qs(url_parts.query)
                        
                        if 'list' in query_params:
                            playlists.append({
                                'title': video_data.get('title', 'Unknown Playlist'),
                                'id': query_params['list'][0],
                                'uploader': channel,
                                'url': url
                            })
                except json.JSONDecodeError:
                    continue
                    
            if playlists:
                # Let user select a playlist
                print("\nFound playlists:")
                for i, playlist in enumerate(playlists, 1):
                    print(f"{i}. {playlist['title']} by {playlist['uploader']}")
                    print(f"   URL: {playlist['url']}")
                
                choice = input("\nSelect a playlist (number) or 'q' to quit: ")
                if choice.lower() == 'q':
                    return None
                
                try:
                    choice = int(choice) - 1
                    if 0 <= choice < len(playlists):
                        return playlists[choice]['id']
                except ValueError:
                    pass
                
                print("Invalid selection")
                return None
        except Exception as e:
            print(f"Channel search failed: {e}")
    
    
    # Search for playlists matching the query
    print(f"Searching for playlists matching: {query}")
    cmd = ["yt-dlp", "--flat-playlist", "--dump-json", "--no-warnings", f"ytsearch5:{query} playlist"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error searching for playlists: {result.stderr}")
            return None
        
        playlists = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            try:
                video_data = json.loads(line)
                # Get the actual YouTube playlist URL and extract ID from it
                if 'url' in video_data and video_data.get('webpage_url'):
                    url = video_data.get('webpage_url', '')
                    if 'youtube.com/playlist' in url or 'list=' in url:
                        url_parts = urlparse(url)
                        query_params = parse_qs(url_parts.query)
                        
                        if 'list' in query_params:
                            playlists.append({
                                'title': video_data.get('title', 'Unknown Playlist'),
                                'id': query_params['list'][0],
                                'uploader': video_data.get('uploader', 'Unknown Uploader'),
                                'url': url
                            })
            except json.JSONDecodeError:
                continue
        
        if not playlists:
            # Fallback: Try direct YouTube search with a different approach
            print("Trying alternative search method...")
            cmd = ["yt-dlp", "--flat-playlist", "--dump-json", "--no-warnings", 
                   f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}+playlist"]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                for line in result.stdout.strip().split('\n'):
                    if not line.strip():
                        continue
                    try:
                        video_data = json.loads(line)
                        if 'url' in video_data and 'list=' in video_data.get('webpage_url', ''):
                            url = video_data.get('webpage_url', '')
                            url_parts = urlparse(url)
                            query_params = parse_qs(url_parts.query)
                            
                            if 'list' in query_params:
                                playlists.append({
                                    'title': video_data.get('title', 'Unknown Playlist'),
                                    'id': query_params['list'][0],
                                    'uploader': video_data.get('uploader', 'Unknown Uploader'),
                                    'url': url
                                })
                    except json.JSONDecodeError:
                        continue
            except Exception as e:
                print(f"Alternative search failed: {e}")
        
        if not playlists:
            print("No playlists found")
            return None
        
        # Let user select a playlist
        print("\nFound playlists:")
        for i, playlist in enumerate(playlists, 1):
            print(f"{i}. {playlist['title']} by {playlist['uploader']}")
            print(f"   URL: {playlist['url']}")
        
        choice = input("\nSelect a playlist (number) or 'q' to quit: ")
        if choice.lower() == 'q':
            return None
        
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(playlists):
                return playlists[choice]['id']
        except ValueError:
            pass
        
        print("Invalid selection")
        return None
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get videos from a playlist
def get_playlist_videos(playlist_id):
    playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
    print(f"Fetching videos from playlist: {playlist_url}")
    cmd = ["yt-dlp", "--flat-playlist", "--dump-json", "--no-warnings", playlist_url]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error fetching playlist: {result.stderr}")
            return None
        
        videos = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            try:
                video_data = json.loads(line)
                videos.append({
                    'title': video_data.get('title', 'Unknown Title'),
                    'id': video_data.get('id'),
                    'duration': video_data.get('duration', 0),
                    'uploader': video_data.get('uploader', 'Unknown Uploader')
                })
            except json.JSONDecodeError:
                continue
        
        return videos
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Format duration in seconds to MM:SS or HH:MM:SS
def format_duration(seconds):
    if not seconds:
        return "Unknown"
    
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"

# Display videos with pagination
def display_videos(videos, page=0, per_page=10):
    if not videos:
        print("No videos found in playlist")
        return None
    
    total_videos = len(videos)
    total_pages = (total_videos + per_page - 1) // per_page
    
    while 0 <= page < total_pages:
        os.system('clear' if os.name == 'posix' else 'cls')
        start_idx = page * per_page
        end_idx = min(start_idx + per_page, total_videos)
        
        print(f"\nShowing videos {start_idx+1}-{end_idx} of {total_videos} (Page {page+1}/{total_pages})")
        print("\nID. Title [Duration]")
        print("-" * 80)
        
        for i in range(start_idx, end_idx):
            video = videos[i]
            print(f"{i+1:3d}. {video['title']} [{format_duration(video['duration'])}]")
        
        print("\nCommands:")
        print("  [1-N]: Play video number N")
        print("  n: Next page")
        print("  p: Previous page")
        print("  s: Search within playlist titles")
        print("  q: Quit")
        
        choice = input("\nEnter command: ").lower()
        
        if choice == 'q':
            return None
        elif choice == 'n':
            page = min(page + 1, total_pages - 1)
        elif choice == 'p':
            page = max(page - 1, 0)
        elif choice == 's':
            search_term = input("Enter search term: ").lower()
            if search_term:
                filtered_videos = [v for v in videos if search_term in v['title'].lower()]
                if filtered_videos:
                    temp_result = display_videos(filtered_videos)
                    if temp_result:
                        return temp_result
                else:
                    print("No videos found matching your search.")
                    input("Press Enter to continue...")
        else:
            try:
                video_idx = int(choice) - 1
                if 0 <= video_idx < total_videos:
                    return videos[video_idx]
                else:
                    print("Invalid video number")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid command")
                input("Press Enter to continue...")
    
    return None

# Play a video with mpv
def play_video(video_id):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"\nPlaying: {video_url}")
    
    try:
        # Ask user for playback method
        print("\nPlayback method:")
        print("1. MPV (default)")
        print("2. yt-dlp with MPV (may be more reliable)")
        choice = input("Choose method [1-2, default=1]: ").strip()
        
        if choice == "2":
            # Using yt-dlp to get the video and pipe to mpv - needs shell=True for piping
            command = f"yt-dlp -f 'bestvideo[height<=1080]+bestaudio/best' --no-warnings -o - {video_url} | mpv -"
            subprocess.run(command, shell=True)
        else:
            # Using mpv directly with its built-in yt-dlp integration
            subprocess.run(["mpv", "--ytdl-format=bestvideo[height<=1080]+bestaudio/best", video_url])
    except Exception as e:
        print(f"Error playing video: {e}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="YouTube Playlist Viewer")
    parser.add_argument("query", nargs="?", help="YouTube playlist URL or search term")
    parser.add_argument("--channel", "-c", help="Specify YouTube channel name")
    parser.add_argument("--direct", "-d", action="store_true", help="Directly use query as a playlist ID")
    args = parser.parse_args()
    
    # Check for required dependencies
    check_dependencies()
    
    # History of played videos
    video_history = []
    
    # Direct playlist ID usage
    if args.direct and args.query:
        playlist_id = args.query
        videos = get_playlist_videos(playlist_id)
        if not videos:
            print(f"Could not fetch videos for direct playlist ID: {playlist_id}")
            return
    else:
        # Handle channel specification
        if args.channel and args.query:
            query = f"{args.channel}:{args.query}"
        else:
            # Get query from arguments or prompt user
            query = args.query
            if not query:
                query = input("Enter YouTube playlist URL or search term: ")
        
        # Get playlist ID
        playlist_id = get_playlist_id(query)
        if not playlist_id:
            return
        
        # Get videos from playlist
        videos = get_playlist_videos(playlist_id)
        if not videos:
            return
    
    # Main loop
    while True:
        # Display videos and get user selection
        selected_video = display_videos(videos)
        if not selected_video:
            # Show history menu when exiting playlist view
            if video_history:
                print("\nRecent watch history:")
                for i, video in enumerate(video_history[:10], 1):
                    print(f"{i}. {video['title']}")
                
                print("\nOptions:")
                print("  [1-N]: Replay video number N from history")
                print("  q: Quit")
                
                choice = input("\nEnter command: ").lower()
                if choice != 'q':
                    try:
                        idx = int(choice) - 1
                        if 0 <= idx < len(video_history):
                            # Play the historical video
                            play_video(video_history[idx]['id'])
                            continue
                    except ValueError:
                        pass
            break
        
        # Add to history and play selected video
        if selected_video not in video_history:
            video_history.insert(0, selected_video)  # Add to beginning of history
        play_video(selected_video['id'])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

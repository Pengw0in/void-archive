import os
import yt_dlp
import subprocess
import threading
import time

def update_timer(start_time, stop_event):
    while not stop_event.is_set():
        elapsed = time.perf_counter() - start_time
        print(f"\rElapsed time: {int(elapsed)} seconds", end="", flush=True)
        time.sleep(1)

def search_and_play_youtube_audio(search_query):
    try:
        print(f"Searching for: {search_query}")
        
        # Configure yt-dlp to search YouTube and get the first result
        ydl_opts = {
            'format': 'bestaudio',
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
            'default_search': 'ytsearch1',  # Search YouTube and limit to 1 result
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract information - ytsearch1 will return a list with one entry
            search_results = ydl.extract_info(search_query, download=False)
            
            # Get the first (and only) entry from search results
            if 'entries' in search_results:
                info_dict = search_results['entries'][0]
            else:
                info_dict = search_results  # Direct result
                
            video_title = info_dict['title']
            video_url = info_dict['webpage_url']  # Original video URL
            audio_url = info_dict['url']  # Direct audio stream URL

            with open("txt.txt", "w")  as file:
                file.write(info_dict['url'])
        
            print(f"Playing: {video_title}")
            print(f"Video URL: {video_url}")
            
            start_time = time.perf_counter()
            
            stop_event = threading.Event()
            timer_thread = threading.Thread(target=update_timer, args=(start_time, stop_event))
            timer_thread.daemon = True
            timer_thread.start()

            player_process = subprocess.Popen(['ffplay', '-nodisp', '-autoexit', audio_url], 
                                             stdout=subprocess.DEVNULL, 
                                             stderr=subprocess.DEVNULL)
            
            try:
                player_process.wait()
            except KeyboardInterrupt:
                player_process.terminate()
                print("\nPlayback stopped.")
            finally:
                # Stop the timer
                stop_event.set()
                timer_thread.join(1)  # Wait up to 1 second for timer thread to finish
                elapsed = time.perf_counter() - start_time
                print(f"\nTotal playback time: {int(elapsed)} seconds")
                
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return None

def main():
    search_query = input("Enter what you want to listen to: ")
    search_and_play_youtube_audio(search_query)

if __name__ == "__main__":
    main()
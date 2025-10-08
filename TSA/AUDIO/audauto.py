import os
import yt_dlp
import subprocess
import time

def download_and_play_youtube_audio(youtube_url):
    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'quiet': True, 'no_warnings': True, 'ignoreerrors': True}) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            video_title = info_dict['title']
            audio_url = info_dict['url']
        
            print(f"Starting to play: {video_title}")
            start_time = time.perf_counter()
            
            player_process = subprocess.Popen(['ffplay', '-nodisp', '-autoexit', audio_url], 
                                             stdout=subprocess.DEVNULL, 
                                             stderr=subprocess.DEVNULL)
            
            try:
                player_process.wait()
            except KeyboardInterrupt:
                player_process.terminate()
                print("\nPlayback stopped.")
            finally:
                elapsed = time.perf_counter() - start_time
                print(f"Total playback time: {int(elapsed)} seconds")
                
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return None

def main():
    youtube_url = input("Enter the YouTube video URL: ")
    download_and_play_youtube_audio(youtube_url)

if __name__ == "__main__":
    main()
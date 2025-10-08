import os
import yt_dlp

def download_youtube_audio(youtube_url, output_path='AUDIO/ytdlp-auds'):
    """
    Download audio from a YouTube video and convert it to WAV format.
    
    Args:
    youtube_url (str): URL of the YouTube video
    output_path (str, optional): Directory to save downloaded files. Defaults to 'downloads'.
    
    Returns:
    str: Path to the converted audio file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '320',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'no_color': True,
        }
        
        # Create a yt-dlp object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info_dict = ydl.extract_info(youtube_url, download=True)
            
            # Get the filename
            video_title = info_dict.get('title', None)
            
            # Find the downloaded file
            for file in os.listdir(output_path):
                if file.endswith('.wav') and video_title.replace('/', '_') in file:
                    wav_filename = os.path.join(output_path, file)
                    print(f"Successfully downloaded audio: {wav_filename} at {output_path}")
                    return wav_filename
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Example usage
    youtube_url = input("Enter the YouTube video URL: ")
    download_youtube_audio(youtube_url)

if __name__ == "__main__":
    main()
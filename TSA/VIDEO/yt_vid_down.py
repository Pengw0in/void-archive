import subprocess
import yt_dlp
import os

# Function to convert .webm to .mp4 using FFmpeg
def convert_to_mp4(input_file, output_file):
    try:
        print(f"Converting {input_file} to {output_file}...")
        command = [
            "ffmpeg",
            "-i", input_file,   # Input file
            "-c:v", "copy",     # Copy video stream
            "-c:a", "aac",      # Convert audio to AAC
            output_file
        ]
        subprocess.run(command, check=True)
        print("Conversion successful!")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Download video using yt_dlp
def download_video(video_url):
    try:
        # Define options for the download
        options = {
            'format': 'bestvideo+bestaudio/best',  # Best video and audio streams
            'outtmpl': '%(title)s.%(ext)s',        # Save as title with correct extension
        }

        # Initialize yt_dlp
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(video_url, download=True)  # Download video

        # Get downloaded file name
        downloaded_file = ydl.prepare_filename(info)
        print(f"Downloaded file: {downloaded_file}")

        # Check if the file is .webm and convert to .mp4
        if downloaded_file.endswith('.webm'):
            mp4_file = downloaded_file.replace('.webm', '.mp4')  # Replace extension
            convert_to_mp4(downloaded_file, mp4_file)

            # Optionally, delete the original .webm file
            os.remove(downloaded_file)
            print(f"Deleted original file: {downloaded_file}")

    except Exception as e:
        print(f"An error occurred during download: {e}")

# Main program
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)

import subprocess
import os
import sys
import re


def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    if not filename or filename == 'NA':
        return "video"

    # Replace invalid characters with underscores
    invalid_chars = r'[\\/*?:"<>|]'
    sanitized = re.sub(invalid_chars, '_', filename)

    # Replace non-ASCII characters
    sanitized = ''.join(c if ord(c) < 128 else '_' for c in sanitized)

    # Limit filename length
    if len(sanitized) > 200:
        sanitized = sanitized[:197] + "..."

    return sanitized or "video"


def download_video(url, output_path="Output"):
    """Download video using yt-dlp"""
    os.makedirs(output_path, exist_ok=True)

    try:
        # First get video info to get title
        cmd_info = [
            "yt-dlp",
            "--skip-download",
            "--print", "title",
            url
        ]
        result = subprocess.run(cmd_info, capture_output=True, text=True)
        title = result.stdout.strip()
        sanitized_title = sanitize_filename(title)

        # Download the video
        output_file = os.path.join(output_path, f"{sanitized_title}.mp4")
        cmd_download = [
            "yt-dlp",
            "--format", "mp4",
            "-o", output_file,
            url
        ]

        print(f"Downloading video...")
        subprocess.run(cmd_download)

        return output_file, sanitized_title

    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None, None


def convert_to_gif(video_file, start_time, duration, output_path="Output", fps=15, width=480, height=240):
    """Convert video segment to GIF using FFmpeg"""
    if not os.path.exists(video_file):
        print(f"Error: Video file not found: {video_file}")
        return None

    os.makedirs(output_path, exist_ok=True)

    # Get base filename without extension
    base_name = os.path.basename(video_file)
    base_name = os.path.splitext(base_name)[0]

    # Create output filename with timestamp info
    gif_file = os.path.join(
        output_path, f"{base_name}_{start_time.replace(':', '_')}_duration_{duration}.gif")

    try:
        # FFmpeg command to convert video segment to GIF
        cmd = [
            "ffmpeg",
            "-y",  # Overwrite output file if exists
            "-i", video_file,  # Input file
            "-ss", start_time,  # Start time
            "-t", duration,  # Duration
            # Filters for high-quality GIF with specific dimensions
            "-vf", f"fps={fps},scale={width}:{height}:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
            "-loop", "0",  # Loop forever
            gif_file
        ]

        print(f"Converting video segment to GIF...")
        subprocess.run(cmd)

        if os.path.exists(gif_file):
            print(f"GIF created successfully: {gif_file}")
            return gif_file
        else:
            print("GIF creation failed")
            return None

    except Exception as e:
        print(f"Error converting to GIF: {str(e)}")
        return None


def get_user_input():
    """Get interactive input from user"""
    print("\n=== Video to GIF Converter ===\n")

    # Get source (URL or file path)
    while True:
        source = input("Enter YouTube URL or local video file path: ").strip()
        if source:
            break
        print("Please enter a valid URL or file path.")

    # Check if the source is a URL or file
    is_url = re.match(r'^https?://', source)

    # Get time parameters
    start_time = input(
        "Enter start time (format: HH:MM:SS) [default: 00:00:00]: ").strip()
    if not start_time:
        start_time = "00:00:00"

    duration = input("Enter duration in seconds [default: 5]: ").strip()
    if not duration:
        duration = "5"

    # Get quality parameters
    fps = input("Enter frames per second [default: 15]: ").strip()
    if not fps:
        fps = "15"

    width = input("Enter output width in pixels [default: 480]: ").strip()
    if not width:
        width = "480"

    height = input("Enter output height in pixels [default: 240]: ").strip()
    if not height:
        height = "240"

    # Get output directory
    output_path = input("Enter output directory [default: Output]: ").strip()
    if not output_path:
        output_path = "Output"

    return {
        "source": source,
        "start_time": start_time,
        "duration": duration,
        "fps": int(fps),
        "width": int(width),
        "height": int(height),
        "output_path": output_path,
        "is_url": bool(is_url)
    }


def main():
    # Get user input
    params = get_user_input()

    # Process source - either download from URL or use local file
    if params["is_url"]:
        print(f"Downloading video from URL...")
        video_file, _ = download_video(params["source"], params["output_path"])
        if not video_file:
            print("Failed to download video. Exiting.")
            return
    else:
        # It's a local file
        if not os.path.exists(params["source"]):
            print(f"Error: Local file not found: {params['source']}")
            return
        video_file = params["source"]

    # Convert to GIF
    convert_to_gif(
        video_file,
        params["start_time"],
        params["duration"],
        params["output_path"],
        params["fps"],
        params["width"],
        params["height"]
    )


if __name__ == "__main__":
    main()

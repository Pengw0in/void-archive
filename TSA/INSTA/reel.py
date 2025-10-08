import instaloader

def download_instagram_reel(url):
    # Initialize Instaloader
    loader = instaloader.Instaloader()
    
    # Login if needed (for private accounts)
    # loader.login("your_username", "your_password")
    
    try:
        # Extract the shortcode from the URL
        shortcode = url.split("/")[-2]

        # Fetch the Reel post
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        # Download the Reel in the highest quality
        loader.download_post(post, target="high_quality_reels")
        print("Reel downloaded successfully in the highest quality!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    reel_url = input("Enter the Instagram Reel URL: ")
    download_instagram_reel(reel_url)

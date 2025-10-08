import requests
from PIL import Image
from io import BytesIO

# URL of the .jfif image
url = "https://doeresults.gitam.edu/photo/img.aspx?id=2024008688"

# Step 1: Download the image
response = requests.get(url)
if response.status_code == 200:
    # Load the image from the response content
    img = Image.open(BytesIO(response.content))
    
    # Step 2: Convert and save as .jpg
    output_path = "2024064631.jpg"  # Save the file locally
    img.convert("RGB").save(output_path, "JPEG")
    print(f"Image successfully saved as {output_path}")
else:
    print(f"Failed to fetch the image. Status code: {response.status_code}")
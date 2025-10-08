import os
import zipfile
from PIL import Image
from pathlib import Path

def cbz_to_pdf(cbz_path, output_pdf_path):
    """
    Converts a CBZ file to a PDF.

    :param cbz_path: Path to the CBZ file.
    :param output_pdf_path: Path to save the output PDF.
    """
    temp_dir = None  # Ensure temp_dir is always defined
    try:
        # Create a temporary directory to extract the CBZ file
        temp_dir = Path("temp_cbz")
        temp_dir.mkdir(exist_ok=True)

        with zipfile.ZipFile(cbz_path, 'r') as cbz_file:
            cbz_file.extractall(temp_dir)

        # Get a sorted list of image files in the temporary directory
        image_files = sorted(temp_dir.glob("*"))
        image_list = []

        # Open the images
        for img_path in image_files:
            with Image.open(img_path) as img:
                # Convert image to RGB (to ensure compatibility with PDF)
                image_list.append(img.convert("RGB"))

        # Save images to a single PDF
        if image_list:
            image_list[0].save(
                output_pdf_path, save_all=True, append_images=image_list[1:]
            )
            print(f"PDF successfully created: {output_pdf_path}")
        else:
            print(f"No images found in the CBZ file: {cbz_path}")

    except Exception as e:
        print(f"Error processing {cbz_path}: {e}")
    finally:
        # Clean up temporary files if temp_dir was created
        if temp_dir and temp_dir.exists():
            for item in temp_dir.iterdir():
                item.unlink()
            temp_dir.rmdir()

if __name__ == "__main__":
    print("CBZ to PDF Converter (Auto Mode)")

    # Get the current directory
    current_dir = Path.cwd()
    print(f"Looking for CBZ files in: {current_dir}")

    # Find all CBZ files in the current directory
    cbz_files = list(current_dir.glob("*.cbz"))

    if not cbz_files:
        print("No CBZ files found in the current directory.")
    else:
        print(f"Found {len(cbz_files)} CBZ file(s):")
        for cbz_file in cbz_files:
            print(f" - {cbz_file.name}")

        # Convert each CBZ file to PDF
        for cbz_file in cbz_files:
            output_pdf = cbz_file.with_suffix(".pdf")
            print(f"Converting {cbz_file.name} to {output_pdf.name}...")
            cbz_to_pdf(cbz_file, output_pdf)

        print("All conversions completed.")

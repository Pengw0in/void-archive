#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os
import numpy as np
from PIL import Image
import argparse

def compute_layers(arr, mode, output_dir, filename):
    """Compute each bit's visual image for a given layer `arr`."""
    for i in range(8):  # 8 bits layer
        newdata = (arr >> i) % 2 * 255  # Highlighting the layer bit `i`
        if mode == 'RGBA':  # Force alpha layer (4th) to 255 if exist
            newdata[:, :, 3] = 255
        
        output_file = os.path.join(output_dir, f"{filename}_{i+1}.png")
        Image.fromarray(newdata, mode).save(output_file)
        print(f"Created bit plane {i+1} for {filename}: {output_file}")

def process_image(input_path, output_dir):
    """Apply compute_layers() on each image layer and save images."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Open image
    img_pil = Image.open(input_path)
    print(f"Processing image: {input_path} (Mode: {img_pil.mode})")

    # Convert all modes to RGBA except RGB images
    if img_pil.mode in ["P", "1", "L", "LA", "RGBX", "RGBa", "CMYK", "LAB",
                        "YCbCr", "HSV", "I", "F"]:
        print(f"Converting {img_pil.mode} to RGBA")
        img_pil = img_pil.convert('RGBA')

    # Get numpy array
    npimg = np.array(img_pil)

    # Generate images from numpy array and save
    print("Extracting bit planes...")
    compute_layers(npimg, img_pil.mode, output_dir, "image_rgb")  # rgb
    compute_layers(npimg[:, :, 0], 'L', output_dir, "image_r")  # r
    compute_layers(npimg[:, :, 1], 'L', output_dir, "image_g")  # g
    compute_layers(npimg[:, :, 2], 'L', output_dir, "image_b")  # b

    # Process alpha channel if present
    if img_pil.mode == "RGBA":
        compute_layers(npimg[:, :, 3], 'L', output_dir, "image_a")  # alpha

    print("Processing complete!")

def main():
    parser = argparse.ArgumentParser(description='Extract bit planes from an image for steganography analysis')
    parser.add_argument('image', help='Path to the image file')
    parser.add_argument('-o', '--output', default='output', help='Output directory for bit planes (default: output)')
    
    args = parser.parse_args()
    
    process_image(args.image, args.output)

if __name__ == "__main__":
    main()

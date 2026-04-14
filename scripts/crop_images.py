#!/usr/bin/env python3
"""
Script to standardize image shapes and remove backgrounds for bakery products.
Crops images to center with consistent aspect ratio.
"""

import os
from PIL import Image

INPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'images')
OUTPUT_DIR = INPUT_DIR

TARGET_SIZE = (800, 800)  # 1:1 square
ASPECT_RATIO = 1 / 1

def crop_center(img, target_size):
    """Crop image from center to target aspect ratio, then resize."""
    width, height = img.size
    target_width, target_height = target_size
    
    # Calculate crop box for target aspect ratio
    current_ratio = width / height
    target_ratio = target_width / target_height
    
    if current_ratio > target_ratio:
        # Image is wider - crop horizontally
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        img = img.crop((left, 0, left + new_width, height))
    else:
        # Image is taller - crop vertically
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        img = img.crop((0, top, width, top + new_height))
    
    # Resize to target
    return img.resize(target_size, Image.Resampling.LANCZOS)

def process_image(input_path, output_path, target_size=TARGET_SIZE):
    """Process a single image - crop and resize."""
    try:
        img = Image.open(input_path)
        
        # Convert RGBA to RGB if needed (for transparency)
        if img.mode == 'RGBA':
            # Create white background for transparent areas
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Crop and resize
        img = crop_center(img, target_size)
        
        # Save
        img.save(output_path, 'PNG', quality=95)
        print(f"Processed: {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def process_all_images():
    """Process all images in the input directory."""
    if not os.path.exists(INPUT_DIR):
        print(f"Input directory not found: {INPUT_DIR}")
        return
    
    # Process all PNG and JPG files
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = input_path  # Overwrite original
            
            if os.path.isfile(input_path):
                process_image(input_path, output_path)

if __name__ == '__main__':
    process_all_images()
    print("Done!")
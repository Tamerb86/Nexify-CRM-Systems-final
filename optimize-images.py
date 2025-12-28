#!/usr/bin/env python3
"""
Image Optimization Script for Nexify Website
- Compresses PNG images
- Converts large PNGs to optimized WebP
- Removes duplicate/original files
- Generates optimized versions
"""

import os
from pathlib import Path
from PIL import Image
import shutil

# Configuration
IMAGE_DIR = Path("/home/ubuntu/nexify-site/public/images")
MAX_WIDTH = 1920  # Max width for large images
QUALITY_WEBP = 85
QUALITY_JPEG = 85
QUALITY_PNG = 85

def get_file_size_mb(path):
    """Get file size in MB"""
    return os.path.getsize(path) / (1024 * 1024)

def optimize_image(input_path, output_path=None, max_width=MAX_WIDTH):
    """Optimize a single image"""
    if output_path is None:
        output_path = input_path
    
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB for JPEG
            if img.mode == 'RGBA' and input_path.suffix.lower() in ['.jpg', '.jpeg']:
                img = img.convert('RGB')
            
            # Resize if too large
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save optimized
            ext = Path(output_path).suffix.lower()
            if ext == '.webp':
                img.save(output_path, 'WEBP', quality=QUALITY_WEBP, optimize=True)
            elif ext in ['.jpg', '.jpeg']:
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img.save(output_path, 'JPEG', quality=QUALITY_JPEG, optimize=True)
            elif ext == '.png':
                img.save(output_path, 'PNG', optimize=True)
            
            return True
    except Exception as e:
        print(f"  Error optimizing {input_path}: {e}")
        return False

def create_webp_version(input_path):
    """Create WebP version of an image"""
    webp_path = input_path.with_suffix('.webp')
    if webp_path.exists():
        return webp_path
    
    try:
        with Image.open(input_path) as img:
            # Resize if too large
            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_height = int(img.height * ratio)
                img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
            
            img.save(webp_path, 'WEBP', quality=QUALITY_WEBP, optimize=True)
            return webp_path
    except Exception as e:
        print(f"  Error creating WebP for {input_path}: {e}")
        return None

def main():
    print("=" * 60)
    print("Image Optimization for Nexify Website")
    print("=" * 60)
    
    # Find all images
    png_files = list(IMAGE_DIR.glob("*.png"))
    jpg_files = list(IMAGE_DIR.glob("*.jpg")) + list(IMAGE_DIR.glob("*.jpeg"))
    webp_files = list(IMAGE_DIR.glob("*.webp"))
    
    print(f"\nFound: {len(png_files)} PNG, {len(jpg_files)} JPG, {len(webp_files)} WebP")
    
    # Calculate total size before
    total_before = sum(get_file_size_mb(f) for f in IMAGE_DIR.glob("*.*") if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.webp'])
    print(f"Total size before: {total_before:.2f} MB")
    
    # Process large PNG files (> 500KB)
    print("\n--- Processing large PNG files ---")
    for png_file in png_files:
        size_mb = get_file_size_mb(png_file)
        if size_mb > 0.5:  # > 500KB
            print(f"\n{png_file.name}: {size_mb:.2f} MB")
            
            # Check if WebP version exists
            webp_path = png_file.with_suffix('.webp')
            if webp_path.exists():
                webp_size = get_file_size_mb(webp_path)
                print(f"  WebP exists: {webp_size:.2f} MB")
                
                # If PNG is much larger than WebP, we can remove PNG
                if size_mb > 1 and webp_size < size_mb * 0.5:
                    # Keep PNG but optimize it
                    optimize_image(png_file)
                    new_size = get_file_size_mb(png_file)
                    print(f"  Optimized PNG: {new_size:.2f} MB")
            else:
                # Create WebP version
                webp_path = create_webp_version(png_file)
                if webp_path:
                    webp_size = get_file_size_mb(webp_path)
                    print(f"  Created WebP: {webp_size:.2f} MB")
    
    # Remove _original files (duplicates)
    print("\n--- Removing duplicate _original files ---")
    original_files = list(IMAGE_DIR.glob("*_original.*"))
    for orig_file in original_files:
        # Check if non-original version exists
        base_name = orig_file.stem.replace('_original', '')
        non_orig = IMAGE_DIR / f"{base_name}{orig_file.suffix}"
        if non_orig.exists():
            size_mb = get_file_size_mb(orig_file)
            print(f"  Removing {orig_file.name} ({size_mb:.2f} MB)")
            orig_file.unlink()
    
    # Calculate total size after
    total_after = sum(get_file_size_mb(f) for f in IMAGE_DIR.glob("*.*") if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.webp'])
    
    print("\n" + "=" * 60)
    print(f"Total size before: {total_before:.2f} MB")
    print(f"Total size after:  {total_after:.2f} MB")
    print(f"Saved: {total_before - total_after:.2f} MB ({((total_before - total_after) / total_before * 100):.1f}%)")
    print("=" * 60)

if __name__ == "__main__":
    main()

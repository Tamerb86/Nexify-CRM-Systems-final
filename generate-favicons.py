#!/usr/bin/env python3
"""Generate favicon files from SVG"""

from PIL import Image, ImageDraw
import os

OUTPUT_DIR = "/home/ubuntu/nexify-site/public"

def create_favicon_png(size, output_path):
    """Create a favicon PNG with gradient background and N letter"""
    # Create image with gradient
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for y in range(size):
        for x in range(size):
            # Calculate gradient color (indigo to teal)
            ratio = (x + y) / (2 * size)
            r = int(79 + (20 - 79) * ratio)  # 4F46E5 to 14B8A6
            g = int(70 + (184 - 70) * ratio)
            b = int(229 + (166 - 229) * ratio)
            
            # Check if within rounded rectangle
            corner_radius = size // 5
            in_rect = True
            
            # Check corners
            if x < corner_radius and y < corner_radius:
                if (x - corner_radius) ** 2 + (y - corner_radius) ** 2 > corner_radius ** 2:
                    in_rect = False
            elif x >= size - corner_radius and y < corner_radius:
                if (x - (size - corner_radius)) ** 2 + (y - corner_radius) ** 2 > corner_radius ** 2:
                    in_rect = False
            elif x < corner_radius and y >= size - corner_radius:
                if (x - corner_radius) ** 2 + (y - (size - corner_radius)) ** 2 > corner_radius ** 2:
                    in_rect = False
            elif x >= size - corner_radius and y >= size - corner_radius:
                if (x - (size - corner_radius)) ** 2 + (y - (size - corner_radius)) ** 2 > corner_radius ** 2:
                    in_rect = False
            
            if in_rect:
                img.putpixel((x, y), (r, g, b, 255))
    
    # Draw N letter
    from PIL import ImageFont
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(size * 0.6))
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), "N", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]
    
    draw.text((x, y), "N", fill="white", font=font)
    
    img.save(output_path, "PNG")
    print(f"Created: {output_path}")

def create_ico(sizes, output_path):
    """Create ICO file with multiple sizes"""
    images = []
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Create gradient background
        for y in range(size):
            for x in range(size):
                ratio = (x + y) / (2 * size)
                r = int(79 + (20 - 79) * ratio)
                g = int(70 + (184 - 70) * ratio)
                b = int(229 + (166 - 229) * ratio)
                
                corner_radius = size // 5
                in_rect = True
                
                if x < corner_radius and y < corner_radius:
                    if (x - corner_radius) ** 2 + (y - corner_radius) ** 2 > corner_radius ** 2:
                        in_rect = False
                elif x >= size - corner_radius and y < corner_radius:
                    if (x - (size - corner_radius)) ** 2 + (y - corner_radius) ** 2 > corner_radius ** 2:
                        in_rect = False
                elif x < corner_radius and y >= size - corner_radius:
                    if (x - corner_radius) ** 2 + (y - (size - corner_radius)) ** 2 > corner_radius ** 2:
                        in_rect = False
                elif x >= size - corner_radius and y >= size - corner_radius:
                    if (x - (size - corner_radius)) ** 2 + (y - (size - corner_radius)) ** 2 > corner_radius ** 2:
                        in_rect = False
                
                if in_rect:
                    img.putpixel((x, y), (r, g, b, 255))
        
        from PIL import ImageFont
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(size * 0.6))
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), "N", font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size - text_width) // 2
        y = (size - text_height) // 2 - bbox[1]
        draw.text((x, y), "N", fill="white", font=font)
        
        images.append(img)
    
    images[0].save(output_path, format='ICO', sizes=[(s, s) for s in sizes])
    print(f"Created: {output_path}")

# Generate favicons
print("Generating favicon files...")

# favicon-16.png
create_favicon_png(16, f"{OUTPUT_DIR}/favicon-16.png")

# favicon-32.png
create_favicon_png(32, f"{OUTPUT_DIR}/favicon-32.png")

# apple-touch-icon.png (180x180)
create_favicon_png(180, f"{OUTPUT_DIR}/apple-touch-icon.png")

# favicon.ico (16, 32, 48)
create_ico([16, 32, 48], f"{OUTPUT_DIR}/favicon.ico")

print("\nAll favicon files generated successfully!")

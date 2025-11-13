#!/usr/bin/env python3
from PIL import Image
import os

# Open the original icon
img = Image.open('static/images/app-icon.png')

# Create a smaller version (64x64)
img_small = img.resize((64, 64), Image.Resampling.LANCZOS)

# Save with optimization
img_small.save('static/images/app-icon-64.png', 'PNG', optimize=True)

print(f"Created optimized 64x64 icon")
print(f"Original size: {os.path.getsize('static/images/app-icon.png')} bytes")
print(f"New size: {os.path.getsize('static/images/app-icon-64.png')} bytes")

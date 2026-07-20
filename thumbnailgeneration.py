import os
from PIL import Image

# Set the input and output directories
input_directory = "input_images/"
output_directory = "thumbnails/"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Loop through each file in the input directory
for filename in os.listdir(input_directory):
    # Check if the file is an image (you can add more image extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        try:
            # Open the image using Pillow
            with Image.open(os.path.join(input_directory, filename)) as img:
                # Resize the image to 50x50 pixels while maintaining aspect ratio
                img.thumbnail((50, 50))
                # Save the thumbnail in the output directory
                img.save(os.path.join(output_directory, filename))
                print(f"Thumbnail created for: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

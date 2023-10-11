from PIL import Image
import os

# Define the input directory containing JPG images and the output directory for PNG images
input_dir = "./images"
output_dir = "./images2"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        # Open the JPG image using Pillow
        img = Image.open(os.path.join(input_dir, filename))

        # Remove the ".jpg" extension and add ".png" for the output filename
        output_filename = os.path.splitext(filename)[0] + ".png"

        # Save the image as PNG in the output directory
        img.save(os.path.join(output_dir, output_filename), "PNG")

print("Conversion complete.")

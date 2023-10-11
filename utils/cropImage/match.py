import os

# Specify the paths to the image and text file directories
image_dir = "./images2"
text_dir = "./labels"

# Get the list of image file names (excluding extensions)
image_files = [os.path.splitext(file)[0] for file in os.listdir(image_dir) if file.endswith((".jpg", ".png", ".jpeg"))]

# Get the list of text file names (excluding extensions)
text_files = [os.path.splitext(file)[0] for file in os.listdir(text_dir) if file.endswith(".txt")]

# Find image files without corresponding text files
missing_text_files = set(image_files) - set(text_files)

# Find text files without corresponding image files
missing_image_files = set(text_files) - set(image_files)

# Print the missing pairs
print("Image files without corresponding text files:")
print(missing_text_files)

print("\nText files without corresponding image files:")
print(missing_image_files)

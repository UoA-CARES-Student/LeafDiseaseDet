import os
import cv2

# Define the input folder containing YOLO format text files and images
input_folder = "./cropInput"
# Define the output folder for cropped images
output_folder = "./output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through YOLO format text files
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        # Read the YOLO format text file
        with open(os.path.join(input_folder, filename), 'r') as file:
            lines = file.readlines()
        
        # Get the image file path by changing the file extension
        image_filename = os.path.splitext(filename)[0] + ".png"  # Assuming images have .jpg extension
        image_path = os.path.join(input_folder, image_filename)
        
        # Load the image using OpenCV
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error loading image: {image_path}")
            continue

        height, width, _ = image.shape
        
        for line in lines:
            data = line.strip().split()
            
            # Ignore the first value (class ID) and unpack the rest
            _, x_center, y_center, bbox_width, bbox_height = map(float, data)
            
            # Convert YOLO format to OpenCV format (top-left x, top-left y, bottom-right x, bottom-right y)
            x1 = int((x_center - bbox_width/2) * width)
            y1 = int((y_center - bbox_height/2) * height)
            x2 = int((x_center + bbox_width/2) * width)
            y2 = int((y_center + bbox_height/2) * height)
            
            # Crop and save the bounding box region if it's valid
            if x1 >= 0 and y1 >= 0 and x2 <= width and y2 <= height:
                cropped_image = image[y1:y2, x1:x2]
                output_filename = os.path.splitext(filename)[0] + f"_class_{int(data[0])}_bbox_{x_center}_{y_center}.jpg"
                output_path = os.path.join(output_folder, output_filename)
                cv2.imwrite(output_path, cropped_image)
            else:
                print(f"Invalid bounding box coordinates in: {image_filename}")

print("Cropping and saving complete.")

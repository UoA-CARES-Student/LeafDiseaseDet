import cv2
import os

# Define the paths for YOLO format files and input images
yolo_format_dir = "./labels"
image_dir = "./images"
output_dir = "./output"

if os.path.exists(yolo_format_dir):
    print("exists")
else:
    print("nono")

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to parse YOLO format lines and return bounding box coordinates
def parse_yolo_line(line, img_width, img_height):
    data = line.strip().split()
    class_id = int(data[0])
    x_center = float(data[1]) * img_width
    y_center = float(data[2]) * img_height
    width = float(data[3]) * img_width
    height = float(data[4]) * img_height

    # Calculate coordinates for cropping
    x1 = int(x_center - width / 2)
    y1 = int(y_center - height / 2)
    x2 = int(x_center + width / 2)
    y2 = int(y_center + height / 2)

    return class_id, x1, y1, x2, y2

# Process each YOLO format file
for yolo_file in os.listdir(yolo_format_dir):
    if yolo_file.endswith(".txt"):
        image_name = os.path.splitext(yolo_file)[0] + ".jpg"  # Assuming images have jpg extension
        yolo_file_path = os.path.join(yolo_format_dir, yolo_file)
        image_path = os.path.join(image_dir, image_name)
        output_image_path = os.path.join(output_dir, image_name)

        # Load the image
        image = cv2.imread(image_path)
        img_height, img_width, _ = image.shape

        # Parse YOLO format file
        with open(yolo_file_path, "r") as yolo_file:
            for line in yolo_file:
                class_id, x1, y1, x2, y2 = parse_yolo_line(line, img_width, img_height)

                # Crop and save the bounding box as a new image
                cropped_image = image[y1:y2, x1:x2]
                output_image_name = f"{class_id}_{os.path.basename(image_path)}"
                output_image_path = os.path.join(output_dir, output_image_name)
                cv2.imwrite(output_image_path, cropped_image)

print("Cropping complete.")
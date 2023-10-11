from PIL import Image
import os

def convert_jpg_to_png(jpg_path, png_path):
    img = Image.open(jpg_path)
    img.save(png_path, "PNG")

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg"):
            jpg_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)
            convert_jpg_to_png(jpg_path, png_path)
        elif filename.lower().endswith(".png"):
            png_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            os.rename(png_path, output_path)

if __name__ == "__main__":
    input_folder = "./convert-yolo-to-pascalvoc/coco/coco128/images/train2017"  # Replace with your input folder path
    output_folder = "./convert-yolo-to-pascalvoc/coco/images"  # Replace with your output folder path
    main(input_folder, output_folder)

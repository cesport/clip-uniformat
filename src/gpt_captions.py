import os
from image_processing import caption_image
from utils import save_to_file, generate_image_path

TARGET_IMAGE_PATH = "/home/cesarportocarrero/clipft/cesar/clip-uniformat/data/val"
OUTPUT_FILE="output_val_0311_captions.txt"

def process_images():
    """Processes all images in a directory and saves the results."""
    i = 0
    directory = os.fsencode(TARGET_IMAGE_PATH)
    for file in os.listdir(directory):
        image_path = os.fsdecode(file)
        full_path = generate_image_path(TARGET_IMAGE_PATH, image_path)
        print(f"Processing: {full_path}")
        raw_result = caption_image(full_path)
        # Save result
        save_to_file(OUTPUT_FILE, f"{raw_result},{image_path}")


if __name__ == "__main__":
    process_images()
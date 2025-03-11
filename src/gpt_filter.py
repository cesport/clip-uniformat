import os
from image_processing import filter_image
from utils import save_to_file, generate_image_path

# Constants (EDIT BASED ON WHAT TO FILTER)
BASE_IMAGE_PATH = "/home/cesarportocarrero/clipft/places365_standard/val/construction_site"
OUTPUT_FILE = "output_val_0311.txt"

def main():
    """Main function to process images and store results."""
    for file in os.listdir(BASE_IMAGE_PATH):
        filename = os.fsdecode(file)
        image_path=generate_image_path(BASE_IMAGE_PATH, filename)
        print(f"Processing: {filename}")
        raw_result = filter_image(image_path)
        # Save result
        save_to_file(OUTPUT_FILE, raw_result)

if __name__ == "__main__":
    main()
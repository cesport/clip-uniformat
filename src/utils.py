import os

def ensure_output_directory(directory="output"):
    """Ensures the output directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_to_file(filename, data):
    """Saves data to a file."""
    ensure_output_directory()
    with open(f"output/{filename}", "a", newline="") as file:
        file.write(data + '\n')

def generate_image_path(base_path, filename):
    """Generates the file path for an image based on an index."""
    return f"{base_path}/{filename}"
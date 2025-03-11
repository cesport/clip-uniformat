import ast
import pandas as pd
import re
import os
import shutil
from utils import generate_image_path

# Define the input file path
BASE_IMAGE_PATH = "/home/cesarportocarrero/clipft/places365_standard/val/construction_site"
TARGET_IMAGE_PATH = "//home/cesarportocarrero/clipft/cesar/clip-uniformat/data/val"
OUTPUT_FILE = "/home/cesarportocarrero/clipft/cesar/clip-uniformat/output/output_val_0311.txt"

# Read the file and parse each line
def extract(input_file):
    data = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            try:
                parsed_line = re.sub("(?<=\w)[‘`’'](?=\w)", '', line)
                parsed_line = ast.literal_eval(parsed_line.strip())  # Safely parse the list format
                if isinstance(parsed_line, list) and len(parsed_line) == 2:
                    data.append(parsed_line)
            except (SyntaxError, ValueError):
                problem=line.strip()
                test=problem[:-1]+"'"+problem[-1:]
                try:
                    parsed_line = ast.literal_eval(test)  # Safely parse the list format
                    if isinstance(parsed_line, list) and len(parsed_line) == 2:
                        data.append(parsed_line)
                except:
                    print(f"Skipping invalid line: {line.strip()}")
    return(data)
df=pd.DataFrame(extract(OUTPUT_FILE), columns=["label", "description"])

def main():
    i=0
    df=pd.DataFrame(extract(OUTPUT_FILE), columns=["label", "description"])
    for file in os.listdir(BASE_IMAGE_PATH):
        if df.iloc[i,0]=="yes":
            filename = os.fsdecode(file)
            source_image_path=generate_image_path(BASE_IMAGE_PATH, filename)
            target_image_path=generate_image_path(TARGET_IMAGE_PATH, filename)
            print(f"Adding: {filename}")
            shutil.copyfile(source_image_path, target_image_path)
        i+=1

if __name__ == "__main__":
    main()

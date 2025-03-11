import pandas as pd
import os
import shutil
from datasets import load_dataset
from collections import Counter, OrderedDict
import matplotlib.pyplot as plt
from utils import generate_image_path

OUTPUT_FILE="/home/cesarportocarrero/clipft/cesar/clip-uniformat/output/output_val_0311_captions.txt"
TARGET_IMAGE_PATH = "/home/cesarportocarrero/clipft/cesar/clip-uniformat/data/val"
DATASET_PATH = '/home/cesarportocarrero/clipft/uf_dataset/val'

uniformat_dict = {
    "A1010": "Standard Foundations",
    "A1020": "Special Foundations",
    "A1030": "Slab on Grade",
    "A2010": "Basement Excavation",
    "A2020": "Basement Walls",
    "B1010": "Floor Construction",
    "B1020": "Roof Construction",
    "B2010": "Exterior Walls",
    "B2020": "Exterior Windows",
    "B2030": "Exterior Doors",
    "B3010": "Roof Coverings",
    "B3020": "Roof Openings",
    "C1010": "Partitions",
    "C1020": "Interior Doors",
    "C1030": "Fittings",
    "C2010": "Stair Construction",
    "C2020": "Stair Finishes",
    "C3010": "Wall Finishes",
    "C3020": "Floor Finishes",
    "C3030": "Ceiling Finishes",
    "D1010": "Elevators & Lifts",
    "D1020": "Escalators & Moving Walks",
    "D1090": "Other Conveying Systems",
    "D2010": "Plumbing Fixtures",
    "D2020": "Domestic Water Distribution",
    "D2030": "Sanitary Waste",
    "D2040": "Rain Water Drainage",
    "D2090": "Other Plumbing Systems",
    "D3010": "Energy Supply",
    "D3020": "Heat Generating Systems",
    "D3030": "Cooling Generating Systems",
    "D3040": "Distribution Systems",
    "D3050": "Terminal & Package Units",
    "D3060": "Controls & Instrumentation",
    "D3070": "Systems Testing & Balancing",
    "D3090": "Other HVAC Systems & Equipment",
    "D4010": "Sprinklers",
    "D4020": "Standpipes",
    "D4030": "Fire Protection Specialties",
    "D4090": "Other Fire Protection Systems",
    "D5010": "Electrical Service & Distribution",
    "D5020": "Lighting and Branch Wiring",
    "D5030": "Communications & Security",
    "D5090": "Other Electrical Systems",
    "E1010": "Commercial Equipment",
    "E1020": "Institutional Equipment",
    "E1030": "Vehicular Equipment",
    "E1090": "Other Equipment",
    "E2010": "Fixed Furnishings",
    "E2020": "Movable Furnishings",
    "F1010": "Special Structures",
    "F1020": "Integrated Construction",
    "F1030": "Special Construction Systems",
    "F1040": "Special Facilities",
    "F1050": "Special Controls and Instrumentation",
    "F2010": "Building Elements Demolition",
    "F2020": "Hazardous Components Abatement"
}

def extract(input_file):
    data = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            if 'jpg' in line:
                elems = line.strip().split(",") #exclude empty lines
                if len(elems)==2:
                    if len(elems[0].split(" ",1)[0])>=5: #exclude lines that do not contain uniformat
                        toapp=[]
                        ufcode=elems[0].split(" ",1)[0][:5]
                        toapp.append(ufcode)
                        if ufcode in uniformat_dict:
                            toapp.append(uniformat_dict[ufcode])
                            toapp.append(elems[1])
                            data.append(toapp)
    return(data)

# Create a DataFrame
df = pd.DataFrame(extract(OUTPUT_FILE), columns=["code", "desc", 'img_path'])

# for i in df['code'].unique():
#     os.mkdir(generate_image_path(DATASET_PATH, i))

for index, row in df.iterrows():
    source=generate_image_path(TARGET_IMAGE_PATH, row["img_path"])
    target=generate_image_path(DATASET_PATH, row["code"]+'/'+row["img_path"])
    shutil.copyfile(source, target)

df.rename(columns={'img_path': 'file_name', 'desc': 'text'}, inplace=True)
df['file_name'] = df['code']+'/'+df['file_name']
df[['file_name','text', 'code']].to_csv(generate_image_path(DATASET_PATH, "metadata.csv"), index=False, header=True)


dataset = load_dataset("imagefolder", data_dir="/home/cesarportocarrero/clipft/uf_dataset")
dataset.push_to_hub("gradient-spaces/uniformat-dataset")

# Count occurrences of each code
code_counts = df["code"].value_counts()

# Plot the bar chart
plt.figure(figsize=(8, 5))
code_counts.plot(kind="bar", color="skyblue", edgecolor="black")

# Customize plot
plt.xlabel("Code")
plt.ylabel("Count")
plt.title("Frequency of Each Code in Dataset")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
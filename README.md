# **🏗️ CLIP fine tuning for Uniformat**
**Finetune CLIP on for atuomatic classification of construction images into Uniformat categories using OpenAI's GPT-4o.**  

---

## **📖 Table of Contents**
- [📌 Overview](#-overview)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📊 Output Format](#-output-format)
- [🔧 Configuration](#-configuration)
- [📌 To-Do & Improvements](#-to-do--improvements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## **📌 Overview**
This project uses OpenAI's **GPT-4o** to classify images of construction sites into **Uniformat** categories. The model analyzes an image and assigns the most appropriate category from a predefined set of construction-related classifications. These images are then used to finetune **CLIP**. The dataset can be found in the Gradient Spaces Hugging Face page [here](https://huggingface.co/datasets/gradient-spaces/uniformat-dataset). 

**💡 Key Features:**
- Uses **GPT-4o** for image classification  
- Encodes images in **Base64** before sending to the API  
- Saves the classification results in a structured format  
- Modularized for easy customization  

---

## **📂 Project Structure**
```console
/clip-uniformat/
│── src                   # Folder with code
│ │── df_hf.py            # Script to create dataset and push to HF  
│ │── gpt_captions.py     # Script to create GPT captions to images
│ │── gpt_filter.py       # Script to use GPT to distinguish construction images
│ │── image_processing.py # Helper functions for OpenAI API
│ │── isolate_images.py   # Script to use the output of gpt_filter.py to drop all non-construction images
│ │── utils.py            # Other helper functions
│── image_processing.py   # Functions for encoding and processing images
│── requirements.txt      # List of dependencies
│── README.md             # Documentation
```
## **⚙️ Installation**
### Set up OpenAI API Key

### **Create a `config.py` File**
In the root directory of your project, create a file named **`config.py`** and add the following code:

```python
from openai import OpenAI

API_KEY = "your-api-key-here"
client = OpenAI(api_key=API_KEY)
```
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
foo@bar:~$ whoami
foo
```
import base64
from config import client

def encode_image(image_path):
    """Encodes an image file as a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def filter_image(image_path):
    """Sends an image to OpenAI API for classification."""
    base64_image = encode_image(image_path)
    prompt_text = (
        "Tell me using a simple 'yes' or 'no' if this image is displaying an active construction site. "
        "Exclude finished construction and people with tools where no specific construction activity is taking place. "
        "Be explicit in your justification. If there are people, make sure they are construction workers. "
        "Return the answer as a Python list: ['yes', 'justification'] or ['no', 'justification']."
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": prompt_text},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
            ]}
        ]
    )

    return completion.choices[0].message.content
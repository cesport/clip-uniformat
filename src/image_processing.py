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

def caption_image(image_path):
    base64_image = encode_image(image_path)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "You are a civil engineer. Tell me which uniformat category this image corresponds to, I want the code and category without quotation marks. This is uniformat in dictionary form:\n\nuniformat_dict = {\n    \"A1010\": \"Standard Foundations\",\n    \"A1020\": \"Special Foundations\",\n    \"A1030\": \"Slab on Grade\",\n    \"A2010\": \"Basement Excavation\",\n    \"A2020\": \"Basement Walls\",\n    \"B1010\": \"Floor Construction\",\n    \"B1020\": \"Roof Construction\",\n    \"B2010\": \"Exterior Walls\",\n    \"B2020\": \"Exterior Windows\",\n    \"B2030\": \"Exterior Doors\",\n    \"B3010\": \"Roof Coverings\",\n    \"B3020\": \"Roof Openings\",\n    \"C1010\": \"Partitions\",\n    \"C1020\": \"Interior Doors\",\n    \"C1030\": \"Fittings\",\n    \"C2010\": \"Stair Construction\",\n    \"C2020\": \"Stair Finishes\",\n    \"C3010\": \"Wall Finishes\",\n    \"C3020\": \"Floor Finishes\",\n    \"C3030\": \"Ceiling Finishes\",\n    \"D1010\": \"Elevators & Lifts\",\n    \"D1020\": \"Escalators & Moving Walks\",\n    \"D1090\": \"Other Conveying Systems\",\n    \"D2010\": \"Plumbing Fixtures\",\n    \"D2020\": \"Domestic Water Distribution\",\n    \"D2030\": \"Sanitary Waste\",\n    \"D2040\": \"Rain Water Drainage\",\n    \"D2090\": \"Other Plumbing Systems\",\n    \"D3010\": \"Energy Supply\",\n    \"D3020\": \"Heat Generating Systems\",\n    \"D3030\": \"Cooling Generating Systems\",\n    \"D3040\": \"Distribution Systems\",\n    \"D3050\": \"Terminal & Package Units\",\n    \"D3060\": \"Controls & Instrumentation\",\n    \"D3070\": \"Systems Testing & Balancing\",\n    \"D3090\": \"Other HVAC Systems & Equipment\",\n    \"D4010\": \"Sprinklers\",\n    \"D4020\": \"Standpipes\",\n    \"D4030\": \"Fire Protection Specialties\",\n    \"D4090\": \"Other Fire Protection Systems\",\n    \"D5010\": \"Electrical Service & Distribution\",\n    \"D5020\": \"Lighting and Branch Wiring\",\n    \"D5030\": \"Communications & Security\",\n    \"D5090\": \"Other Electrical Systems\",\n    \"E1010\": \"Commercial Equipment\",\n    \"E1020\": \"Institutional Equipment\",\n    \"E1030\": \"Vehicular Equipment\",\n    \"E1090\": \"Other Equipment\",\n    \"E2010\": \"Fixed Furnishings\",\n    \"E2020\": \"Movable Furnishings\",\n    \"F1010\": \"Special Structures\",\n    \"F1020\": \"Integrated Construction\",\n    \"F1030\": \"Special Construction Systems\",\n    \"F1040\": \"Special Facilities\",\n    \"F1050\": \"Special Controls and Instrumentation\",\n    \"F2010\": \"Building Elements Demolition\",\n    \"F2020\": \"Hazardous Components Abatement\"\n}"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
        ]}
    ]
    )
    return(completion.choices[0].message.content)
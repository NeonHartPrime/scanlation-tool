import base64
import io
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
MODEL_NAME = "gemma-3-4b"

def image_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()

def translate_image(img):
    img_b64 = image_to_base64(img)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Traduce al español el texto de la imagen. Solo responde en español."},
                    {"type": "image_url", "image_url": {"url": img_b64}}
                ]
            }
        ]
    )

    return response.choices[0].message.content.strip()
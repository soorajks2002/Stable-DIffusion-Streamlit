import requests
from api_key import hugging_face_api_key
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {hugging_face_api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response

def generate_image(prompt) : 
        
    image_bytes = query({"inputs": prompt})

    result_format = {"generation_successful":False, "image":None}

    if image_bytes.status_code == 200 :
        print(image_bytes.content)
        
        image = Image.open(io.BytesIO(image_bytes.content))
        
        result_format["generation_successful"] = True
        result_format["image"] = image
        
        return result_format
        
    else :
        return result_format
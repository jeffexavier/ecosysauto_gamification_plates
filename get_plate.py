import requests
import os

from image_to_base64 import image_to_base64
from dotenv import load_dotenv

load_dotenv()

def get_plate(image_base64):
  try:
    r = requests.post(os.environ.get('VEHICLE_DETECT_ENDPOINT'),
                      data={
                        "image_base64": image_base64 
                      },
                      headers={
                        "authorization": os.environ.get('AUTH_TOKEN')
                      })
    return r.json()
  except Exception as e:
    return f"Aconteceu um erro: {e}"

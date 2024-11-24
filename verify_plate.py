import requests
import os

from dotenv import load_dotenv
# from get_plate import get_plate
# from image_to_base64 import image_to_base64

load_dotenv()

def verify_plate(plate_value):
  try:
    r = requests.get(f'{os.environ.get("VEHICLE_CHECK_ALL_ENDPOINT")}{plate_value}',
                     headers = {
                       'authorization': os.environ.get('AUTH_TOKEN')
                     })
    return r.json()
  except Exception as e:
    return e

import requests
import os

# from verify_plate import verify_plate
# from get_plate import get_plate
# from image_to_base64 import image_to_base64
from dotenv import load_dotenv

load_dotenv()

def get_price(version_id, km):
  try:
    headers = {
      'authorization' : os.environ.get('AUTH_TOKEN')
    }
    payload = {
      'version_id': version_id,
      'km': km,
      'state': 'DF'
    }
    r = requests.get('https://alek-vendas.back.stage.ecosysauto.com.br/api/v1/integrator/price', params = payload, headers = headers)
    return r.json()
  except Exception as e:
    return e

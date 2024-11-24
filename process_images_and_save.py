import os
import json
from image_to_base64 import image_to_base64
from get_plate import get_plate
from verify_plate import verify_plate
from get_price import get_price
from PIL import Image

def process_images_and_save():
  project_root = os.path.dirname(os.path.abspath(__file__))
  images_dir = os.path.join(project_root, "images")
  output_dir = os.path.join(project_root, "output")
  json_output_file = os.path.join(output_dir, "plates.json")

  os.makedirs(output_dir, exist_ok=True)

  if os.path.exists(json_output_file):
    with open(json_output_file, "r", encoding="utf-8") as file:
      results = json.load(file)
  else:
    results = []

  for image_file in os.listdir(images_dir):
    if image_file.lower().endswith((".jpg", ".png", ".jpeg")):
      image_path = os.path.join(images_dir, image_file)

      try:
        image_base64 = image_to_base64(image_path)
        plate_value = get_plate(image_base64)
        plate_data = verify_plate(plate_value['plate'])
        price = get_price(plate_data['data']["vehicle_version_id"], 100000)

        if not price == None:
          new_image_path= os.path.join(output_dir, f"{plate_value['plate']}.jpg")

          if not os.path.exists(new_image_path):
            image = Image.open(image_path)
            image.save(new_image_path)
            results.append({
              "plate": plate_value['plate'],
              "image_file": new_image_path,
              "plate_data": plate_data,
              "price": price
            })

            with open(json_output_file, "w", encoding="utf-8") as file:
              json.dump(results, file, ensure_ascii=False, indent=4)
            
            print(f"Resultados salvos em {json_output_file}")

          else:
            print(f"Placa '{plate_value['plate']}' já analisada com base na imagem {image_file}")

        else:
          print(f"Não foram encontrados preços para a placa {plate_value['plate']}")

      except KeyError as e:
          print(f"Erro: Resposta não contém a chave '{e}' para a imagem {image_file}.")
      except Exception as e:
          print(f"Erro geral ao processar {image_file}: {e}")

process_images_and_save()

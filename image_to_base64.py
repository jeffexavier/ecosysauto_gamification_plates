import base64

def image_to_base64(image_path):
  try:
    with open(image_path, 'rb') as image_file:
      base64_string = base64.b64encode(image_file.read()).decode('utf-8')
      return base64_string
  except FileNotFoundError:
    return "Arquivo não encontrado. Verifique o caminho da imagem"
  except Exception as e:
    return f"Erro ao converter imagem: {e}"

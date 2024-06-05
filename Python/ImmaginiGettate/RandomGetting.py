import os
import requests
from PIL import Image
from io import BytesIO

# Imposta il percorso della directory delle immagini
image_path = "./photo/"

# Crea la directory se non esiste
if not os.path.exists(image_path):
    os.makedirs(image_path)

def download_random_image():
    # URL di Lorem Picsum per ottenere un'immagine casuale
    url = "https://picsum.photos/200/300"
    
    # Effettua una richiesta GET all'URL
    response = requests.get(url)
    
    # Verifica se la richiesta è andata a buon fine
    if response.status_code == 200:
        # Apri l'immagine usando PIL
        image = Image.open(BytesIO(response.content))
        
        # Salva l'immagine sul disco locale
        image.save(os.path.join(image_path, "giggino.jpg"))
        print("Immagine scaricata e salvata come giggino.jpg")
    else:
        print(f"Errore durante il download dell'immagine: {response.status_code}")

# Scarica un'immagine casuale
download_random_image()


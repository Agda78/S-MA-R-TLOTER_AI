import requests
from PIL import Image
from io import BytesIO

image_path = "C:\\Users\\HP\\Documents\\Prova\\S-MA-R-TLOTER_AI\\MATLAB\\Immagini\\"

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
        image.save(image_path + "giggino.jpg")
        print("Immagine scaricata e salvata come random_image.jpg")
    else:
        print(f"Errore durante il download dell'immagine: {response.status_code}")

# Scarica un'immagine casuale
download_random_image()

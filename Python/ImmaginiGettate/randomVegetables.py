import requests
from bs4 import BeautifulSoup
import os

def download_images(url, folder_path, num_images):
    # Creo la cartella se non esiste
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    image_tags = soup.find_all('img')
    for i, image_tag in enumerate(image_tags):
        if i == num_images:
            break
        image_url = image_tag.get('src')
        if image_url:
            # Ottengo solo il nome del file dall'URL
            image_name = os.path.basename(image_url)
            image_path = os.path.join(folder_path, image_name)
            # Scarico l'immagine
            with open(image_path, 'wb') as f:
                response = requests.get(image_url)
                f.write(response.content)
                print(f"Immagine scaricata: {image_path}")

# URL di un sito con immagini di verdure
url = 'https://www.freeimages.com/search/vegetables'
# Cartella in cui salvare le immagini
folder_path = 'C:\\Users\\HP\\Documents\\Prova\\S-MA-R-TLOTER_AI\\MATLAB\\Immagini\\'
# Numero di immagini da scaricare
num_images = 5

download_images(url, folder_path, num_images)
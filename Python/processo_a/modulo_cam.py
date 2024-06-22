import requests
from PIL import Image
from io import BytesIO

def photo_request(esp32_cam_ip, PATH_TOT):
    # URL di richiesta per scattare una foto
    url = f'{esp32_cam_ip}/capture'

    # Invia la richiesta per ottenere l'immagine
    response = requests.get(url)

    if response.status_code == 200:
        print("Foto ricevuta con successo")
        # Salva l'immagine su disco
        with open(PATH_TOT, "wb") as file:
            file.write(response.content)
        print(f"Foto salvata come: {PATH_TOT}")

        # Carica e visualizza l'immagine
        image = Image.open(BytesIO(response.content))
        #image.show()
    else:
        print("Errore nella ricezione della foto. Codice di stato:", response.status_code)
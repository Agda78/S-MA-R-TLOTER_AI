import requests
from PIL import Image
from io import BytesIO
import sys
import socket

numero = str(sys.argv[1])
PATH = '/home/jsorel/Desktop/'
PATH_TOT = PATH+'snapshot'+numero+'.jpg'
# Indirizzo IP dell'ESP32-CAM
esp32_cam_ip = 'http://192.168.188.4'  # Modifica questo con l'IP della tua ESP32-CAM
process_port= 6060


def interpreta(recv_data):
    if(recv_data == 0):
        print("Nessun oggetto rilevato!")
    else:
        print("Rilevato oggetto!")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Aspetta il segnale dall'ultrasuoni 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', process_port))
    server_socket.listen(1)
    print(f"Server in ascolto sulla porta {process_port}")      
    client_socket, client_address = server_socket.accept()
    print(f"Connessione da {client_address}")

    try:
        data = client_socket.recv(1).decode('utf-8')
        if data:
            print(f"Ricevuto {data}")
            interpreta(data)
        else:
            print("Nessun dato ricevuto")
    finally:
        client_socket.close()
        print(f"Connessione con {client_address} chiusa")

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
import socket
import sys
import os 

SAVE_PATH = sys.argv[1]
img_number = sys.argv[2] 
process_port= 5050
cam_ip = '192.168.1.34'
cam_port_send = 80


def interpreta(recv_data):
    if(recv_data == 0):
        print("Nessun oggetto rilevato!")
    else:
        print("Rilevato oggetto!")
def save_image(image_data, image_number):
    file_path = os.path.join(SAVE_PATH, f'received_image_{image_number}.jpg')
    with open(file_path, 'wb') as f:
        f.write(image_data)
    print(f"Image saved at {file_path}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Aspetta il segnale dall'ultrasuoni 
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

#Richiede una foto all'ESP32_CAM

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_client:
        # Connessione al server specificato
        sock_client.connect((cam_ip, cam_port_send))
        
        # Conversione dell'intero in una stringa di byte
        message = str(data).encode('utf-8')
        
        # Invio del messaggio al server
        sock_client.sendall(message)
        
        # Ricezione della conferma dal server (opzionale)
        #data = sock_client.recv(1024)
        #print(f"Ricevuto dal server: {data.decode('utf-8')}")

#ricezione della foto dall' ESP32_CAM

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
        sock_server.bind(('0.0.0.0', process_port))
        sock_server.listen()
        print(f"Listening")

        
        esp_32_conn, esp_32_addr = sock_server.accept()
        with esp_32_conn:
            print(f"Connected by {esp_32_addr}")
            
            # First 4 bytes are the size of the image
            data = esp_32_conn.recv(4)
            img_size = int.from_bytes(data, 'big')
            
            # Now read the image data based on the size
            image_data = b''  # Initialize an empty byte string to store the incoming image data
            while len(image_data) < img_size:
                packet = esp_32_conn.recv(img_size - len(image_data))
                if not packet:
                    break
                image_data += packet  # Append each received packet to image_data
            
            save_image(image_data, img_number)  # Save the complete image data to a file


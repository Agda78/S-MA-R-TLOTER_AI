import socket
import os
import sys

HOST = '0.0.0.0'  # Ascolta su tutte le interfacce
PORT = 1234  # Cambia questo a una porta diversa se necessario
SAVE_PATH = sys.argv[1]

def save_image(image_data, image_number):
    file_path = os.path.join(SAVE_PATH, f'received_image_{image_number}.jpg')
    with open(file_path, 'wb') as f:
        f.write(image_data)
    print(f"Image saved at {file_path}")

def main():
    image_number = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}") 
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                
                #i primi 4 byte sono la dimensione dell'immagine
                data = conn.recv(4)
                img_size = int.from_bytes(data, 'big')
                
                #Leggi l'immagine basandoti sulla dimensione comunicata
                image_data = b''  # Initialize an empty byte string to store the incoming image data
                while len(image_data) < img_size:
                    packet = conn.recv(img_size - len(image_data))
                    if not packet:
                        break
                    image_data += packet
                
                save_image(image_data, image_number)
                image_number += 1 

if __name__ == '__main__':
    os.makedirs(SAVE_PATH, exist_ok=True)
    main()

import socket
import os

HOST = '0.0.0.0'  # Ascolta su tutte le interfacce
PORT = 5011  # Cambia questo a una porta diversa se necessario
SAVE_PATH = '******'  # Sostituisci con il percorso desiderato

def save_image(image_data, image_number):
    file_path = os.path.join(SAVE_PATH, f'received_image_{image_number}.jpg')
    with open(file_path, 'wb') as f:
        f.write(image_data)
    print(f"Image saved at {file_path}")

def main():
    image_number = 0  # Contatore per i file delle immagini

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                
                # First 4 bytes are the size of the image
                data = conn.recv(4)
                img_size = int.from_bytes(data, 'big')
                
                # Now read the image data based on the size
                image_data = b''  # Initialize an empty byte string to store the incoming image data
                while len(image_data) < img_size:
                    packet = conn.recv(img_size - len(image_data))
                    if not packet:
                        break
                    image_data += packet  # Append each received packet to image_data
                
                save_image(image_data, image_number)  # Save the complete image data to a file
                image_number += 1  # Increment the image counter

if __name__ == "__main__":
    # Ensure the SAVE_PATH exists
    os.makedirs(SAVE_PATH, exist_ok=True)
    main()

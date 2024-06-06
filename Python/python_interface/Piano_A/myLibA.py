import socket
import logging
import signal
import sys

# Tale funzione si mette in ascolto del segnale proveniente dall'ultrasuoni
def start_servo_server(port=5000):
    host = "0.0.0.0"
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')  # Rimuovi la data e l'ora
    # Signal handler for graceful shutdown
    def signal_handler(sig, frame):
        logging.info('[Ultrasuoni-Server] Shutting down the server...')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            s.listen()
            logging.info(f"[Ultrasuoni-Server] Server listening on {host}:{port}")
            received_int = 10
            while received_int > 7:
                conn, addr = s.accept()
                with conn:
                    print(f"[Ultrasuoni-Server] Connected by {addr}")
                    data = conn.recv(1024)
                    received_int = int(data.decode().strip())

                    print(f"[Ultrasuoni-Server] Received data: {data.decode()}")
        except Exception as e:
            logging.error(f"[Ultrasuoni-Server] An error occurred: {e}")
        finally:
            s.close()
            logging.info("[Ultrasuoni-Server] Server socket closed")

def print_test():
    print("[ESP32-Client] ESP32-CAM request")

def memory_test(image_path, image_name):
    print("[ESP32-Client] Memorizzazione foto su: " + image_path + image_name)
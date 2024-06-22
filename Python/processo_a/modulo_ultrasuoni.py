import socket
import modulo_generico as gen

def server(process_port):
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
                gen.interpreta(data)
            else:
                print("Nessun dato ricevuto")
        finally:
            client_socket.close()
            print(f"Connessione con {client_address} chiusa")
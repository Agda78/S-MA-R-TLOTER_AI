import socket 
import modulo_generico as gen

def send_forcing(servo_ip, servo_port, forzamento_servo):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_client:
        
        # Connessione al server specificato
        sock_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_client.connect((servo_ip, servo_port))

        # Print per il debugging
        print("Connessione effettuata con successo. Invio forzamento...")

        # Impostazione del messaggio da inviare
        messaggio = gen.message_refactoring(forzamento_servo)

        # Invio effettivo del messaggio
        sock_client.sendall(messaggio.encode('utf-8'))
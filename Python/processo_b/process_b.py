import sys 
import socket 

servo_ip = '192.168.1.29'
servo_port = 80

forzamento_servo = sys.argv[1]

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_client:
            # Connessione al server specificato
            sock_client.connect((servo_ip, servo_port))
            print("Connessione effettuata con successo. Invio forzamento...")
            if forzamento_servo == 'plastica':
                number = 0
                message = number.to_bytes(4, 'big')
                # Invio del messaggio al server
                sock_client.sendall(message)
                break
            elif forzamento_servo == 'carta':
                number = 1
                message = number.to_bytes(4, 'big')
                # Invio del messaggio al server
                sock_client.sendall(message)
                break
            elif forzamento_servo == 'vuoto':
                number = 2
                message = number.to_bytes(4, 'big')
                # Invio del messaggio al server
                sock_client.sendall(message)
                break
            else :
                print("Errore")
                break
        
        # Ricezione della conferma dal server (opzionale)
        #data = sock_client.recv(1024)
        #print(f"Ricevuto dal server: {data.decode('utf-8')}")
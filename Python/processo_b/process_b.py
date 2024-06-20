import sys 
import socket 

servo_ip = '192.168.188.3'
servo_port = 5050

forzamento_servo = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_client:
        # Connessione al server specificato
        sock_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_client.connect((servo_ip, servo_port))
        print("Connessione effettuata con successo. Invio forzamento...")
        if forzamento_servo == 'plastica':
            number = 0
            message = number.to_bytes(4, 'big')
            # Invio del messaggio al server
            sock_client.sendall(message)
            
        elif forzamento_servo == 'carta':
            number = 1
            message = number.to_bytes(4, 'big')
            # Invio del messaggio al server
            sock_client.sendall(message)
            
        elif forzamento_servo == 'vuoto':
            number = 2
            message = number.to_bytes(4, 'big')
            # Invio del messaggio al server
            sock_client.sendall(message)
            
        else:
            print("Errore")
        sock_client.close()
            
    

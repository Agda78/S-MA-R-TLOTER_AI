import sys 
import socket 
import struct

servo_ip = '192.168.188.3'
servo_port = 5050

forzamento_servo = sys.argv[1]
# print(forzamento_servo)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_client:
    # Connessione al server specificato
    sock_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_client.connect((servo_ip, servo_port))
    print("Connessione effettuata con successo. Invio forzamento...")
    if forzamento_servo == 'plastica':
        print("plastica")
        numero = 0
        messaggio = str(numero)+'\n'
        sock_client.sendall(messaggio.encode('utf-8'))

        
    elif forzamento_servo == 'carta':
        print("carta")            
        numero = 1
        messaggio = str(numero)+'\n'
        sock_client.sendall(messaggio.encode('utf-8'))

        
    elif forzamento_servo == 'vuoto':
        numero = 2
        messaggio = str(numero)+'\n'
        sock_client.sendall(messaggio.encode('utf-8'))
    else:
        print("Errore")
# sock_client.close()
            
    

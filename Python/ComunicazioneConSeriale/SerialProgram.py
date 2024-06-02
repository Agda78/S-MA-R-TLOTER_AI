import serial
import time

# Configurazione della porta seriale (modifica la porta con quella corretta per il tuo Arduino)
arduino_port = 'COM13'  # Ad esempio, su Windows potrebbe essere 'COM3'
baud_rate = 9600

# Inizializzazione della connessione seriale
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Attendere che la connessione seriale si stabilizzi

def send_command(command):
    # Invia il comando all'Arduino
    ser.write(f"{command}\n".encode())
    time.sleep(0.5)  # Attendere una risposta
    # Legge la risposta dell'Arduino
    response = ser.readline().decode().strip()
    return response

def main():
    print("Programma di controllo Arduino via seriale. Inserisci 'ON', 'OFF' o 'GET' per interagire.")
    while True:
        command = input("Inserisci comando (ON/OFF/GET/EXIT): ").strip().upper()
        if command == "EXIT":
            print("Chiusura del programma.")
            break
        elif command in ["ON", "OFF", "GET"]:
            response = send_command(command)
            print(f"Arduino risponde: {response}")
        else:
            print("Comando non valido. Riprova.")

if __name__ == "__main__":
    main()

# Chiusura della connessione seriale
ser.close()

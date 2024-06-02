import serial
import time
import sys

# Configurazione della porta seriale (modifica la porta con quella corretta per il tuo Arduino)
# arduino_port = 'COM13'  # Ad esempio, su Windows potrebbe essere 'COM3'
# baud_rate = 9600

# Inizializzazione della connessione seriale

# time.sleep(2)  # Attendere che la connessione seriale si stabilizzi

def send_command(command, ser):
    # Invia il comando all'Arduino
    ser.write(f"{command}\n".encode())
    time.sleep(0.5)  # Attendere una risposta
    # Legge la risposta dell'Arduino
    response = ser.readline().decode().strip()
    return response

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].strip().upper()
        arduino_port = sys.argv[2]
        baud_rate = int(sys.argv[3])
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        time.sleep(2)  # Attendere che la connessione seriale si stabilizzi

        if command in ["ON", "OFF", "GET"]:
            response = send_command(command, ser)
            print(response)
        else:
            print("Comando non valido. Usa ON, OFF o GET.")
    else:
        print("Per favore fornisci un comando (ON, OFF, GET).")

# Chiusura della connessione seriale
ser.close()

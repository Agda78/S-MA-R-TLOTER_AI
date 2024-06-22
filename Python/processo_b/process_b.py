# Libreria di sistema
import sys

# Import del modulo utilizzato per il servo
import modulo_servo as servo

# Setting dei dati della comunicazione con il modulo servo
servo_ip = '192.168.188.3'
servo_port = 5050

# Prelievo del forzamento gettato dalla chiamata della funzione
forzamento = sys.argv[1]

# Invio del forzamento definitivo
servo.send_forcing(servo_ip, servo_port, forzamento)
            
    

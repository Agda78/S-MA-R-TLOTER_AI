# Import delle librerie utili alla comunicazione
from myLibA import *

# !AGGIUNTIVO!
# Se si riesce implementare le funzioni in un file a parte e poi ricostruire qui il main
# in modo da rendere il codice più leggibile e modulare

# Dati di comunicazione con il MATLAB
image_path = "./Napoli"
image_name = "/Carlo.jpg"


# Dati di comunicazione con la scheda
porto_attesa_ultrasuoni = 5000
porto_comunicazione_cam = 4545


if __name__ == "__main__":
    
    
    # Definire la ciclicità del Processo A

    # Attesa del segnale dall'ultasuoni
    start_servo_server(porto_attesa_ultrasuoni)

    # Getting dell'immagine dalla ESP32-CAM
    print_test()

    # Memorizzazione della foto sulla cartella image_path con il nome image_name
    memory_test(image_path, image_name)

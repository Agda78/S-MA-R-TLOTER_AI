# Libreria di sistema
import sys

# Moduli di controllo
import modulo_cam as cam
import modulo_ultrasuoni as ultrasuoni

# Firma per la chiamata da terminale
# python processo_a_2.py <path-comunicazione-foto.jpg>

# In numero dev'essere passato il path di comunicazione e foto . jpg
photo_phat = str(sys.argv[1])

# PATH = '/home/jsorel/Desktop/'
PATH_TOT = photo_phat

# Indirizzo IP dell'ESP32-CAM
esp32_cam_ip = 'http://192.168.188.4'  # Modifica questo con l'IP della tua ESP32-CAM
process_port = 6060

# Processo si mette in attesa di essere contattato sulla
# process_port, quando l'ultrasuoni lo ha contattato, si blocca
ultrasuoni.server(process_port)

# Processo manda una richiesta di foto alla ESP32-CAM che
# la salverà nel luogo prefissato
cam.photo_request(esp32_cam_ip, PATH_TOT)

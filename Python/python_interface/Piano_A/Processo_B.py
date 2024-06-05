#Processo B: Il processo B provvede a ricevere in ingresso il risultato del matlab
#	tramite le sue args, e tramite tali informazioni, va a dare un segnale alla Board che gestisce
#	il servo per fargli attuare i risultati dell'analisi

# Import delle librerie utilitarie
import sys # Funzione per gettare gli args


port_servo_comunication = 8080

# Informazione passata dal MATLAB
information = sys.argv[1]

# Invio dell'informazione al servo

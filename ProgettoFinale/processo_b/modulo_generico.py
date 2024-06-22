
def message_refactoring(forzamento_servo):
    numero = 2
    if forzamento_servo == 'plastica':
        print("plastica")
        numero = 0

    elif forzamento_servo == 'carta':
        print("carta")            
        numero = 1
        
    elif forzamento_servo == 'vuoto':
        numero = 2
        
    else:
        print("Errore")

    return str(numero)+'\n'
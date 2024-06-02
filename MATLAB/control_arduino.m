function result = control_arduino(command, com_port, baud_rate)
    % Specifica il percorso dell'eseguibile Python e dello script
    pythonScript = 'C:\Users\HP\Documents\Prova\S-MA-R-TLOTER_AI\Python\ComunicazioneConSeriale\Serial.py';  % Sostituisci con il percorso del tuo script Python

    % Costruisci il comando di sistema
    cmd = sprintf('python %s %s %s %d', pythonScript, command, com_port, baud_rate);
    
    % Esegui il comando di sistema e cattura l'output
    [status, result] = system(cmd);
    
    % Verifica se ci sono stati errori nell'esecuzione del comando
    if status ~= 0
        error('Errore durante l''esecuzione del comando: %s', result);
    end
    
    % Rimuove eventuali caratteri di nuova linea dall'output
    result = strtrim(result);
end
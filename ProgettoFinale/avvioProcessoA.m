function avvioProcessoA(process_path, image_path)
    % Costruisci il comando di sistema
    cmd = sprintf('python %s %s', process_path, image_path);
    
    % Esegui il comando di sistema e cattura l'output
    [status, result] = system(cmd);
    
    disp(result)
    % Verifica se ci sono stati errori nell'esecuzione del comando
    if status ~= 0
        error('Errore durante l''esecuzione del comando: %s', result);
    end
    
    % Rimuove eventuali caratteri di nuova linea dall'output
    strtrim(result);

end
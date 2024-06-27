function avvioProcessoB(path, forzamento)        
<<<<<<< HEAD
    % Costruisci il comando di sistema
    cmd = sprintf('python %s %s', path, forzamento);
=======
        % Costruisci il comando di sistema
    cmd = sprintf('python3 %s %s', path, forzamento);
>>>>>>> 5d704893e29d226cb006dda4c7d10c69c0032c3a
    
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
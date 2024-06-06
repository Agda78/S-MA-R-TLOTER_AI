fprintf("[MATLAB] Avvio del processo\n");

% Inizializzazione di variabili e caricamento del modello preTrainato

model_path = "";
model_name = "";

model = model_path + model_name;

% load(model, "net");

% Location delle immagini
image_path = "";
image_name = "";

image = image_path + image_name;

% Path del Processo A
path_proc_A = "";

% Path del Processo B
path_proc_B = "";

% Definizione del tempo di pausa in secondi (consentiti anche float)
tempo_pausa = 1;

% Avvio del processo A con rilascio
% Esso si occupa di aggiornare l'immagine

% LOOP: 
fprintf("[MATLAB] Avvio del LOOP sistematico\n");
while true
    try
        % Avviare l'analisi della foto predestinata

        % Analisi tramite la rete preloaddata

        % Analisi del risultato

        % se il risultato è rilevante, allora avvia processo B
        
        % Attesa tra un iterazione e l'altra
        fprintf("[MATLAB] Attesa\n");
        pause(tempo_pausa);
        
    catch
        disp("[MATLAB] Loop interrotto manualmente\n");
        break; % Esci dal loop se viene generata un'eccezione
    end
end

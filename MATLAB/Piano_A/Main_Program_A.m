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
path_proc_A = "C:\Users\HP\Documents\Progetto_TIAI\S-MA-R-TLOTER_AI\Python\python_interface\Piano_A\Processo_A.py";

% Path del Processo B
path_proc_B = "C:\Users\HP\Documents\Progetto_TIAI\S-MA-R-TLOTER_AI\Python\python_interface\Piano_A\Processo_B.py";

% LOOP: 
fprintf("[MATLAB] Avvio del LOOP sistematico \n");
while true
    try
        fprintf("[MATLAB] Avvio del processo A \n");
        % Stringa di avvio del processo A
        avvioProcessoA(path_proc_A)

        % Elaborazione con la rete neurale
        information = "plastic";

        % Impaccottamento dei risultati

        % Stringa di avvio del processo B
        % con in ingresso l'informazione elaborata
        avvioProcessoB(path_proc_B, information)
    catch
        disp("[MATLAB] Loop interrotto manualmente\n");
        break; % Esci dal loop se viene generata un'eccezione
    end
end

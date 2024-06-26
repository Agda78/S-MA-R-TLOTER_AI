fprintf("[MATLAB] Avvio del processo\n");

% Inizializzazione di variabili e caricamento del modello preTrainato

model_path = "ReteTrainata/";
model_name = "Binnet_2.mat";

model = model_path + model_name;

load(model, "trainedNet");

% Location delle immagini
image_path = "./image/";
image_name = "munnezz.jpg";

image = image_path + image_name;

% Path del Processo A
path_proc_A = "./processo_a/process_a_2.py";

% Path del Processo B
path_proc_B = "./processo_b/process_b.py";

% LOOP: 
fprintf("[MATLAB] Avvio del LOOP sistematico \n");
while true
    try
        fprintf("[MATLAB] Avvio del processo A \n");
        % Stringa di avvio del processo A
        avvioProcessoA(path_proc_A, image)

        % Elaborazione con la rete neurale
        % Caricare la nuova immagine
        newImage = imread(image);
        
        % Ridimensionare l'immagine alla dimensione richiesta dalla rete
        inputSize = trainedNet.Layers(1).InputSize;
        resizedImage = imresize(newImage, [inputSize(1) inputSize(2)]);
        
        % Classificare l'immagine
        [label, scores] = classify(trainedNet, resizedImage);
        
        % Impaccottamento dei risultati
        forzamento = char(label);

        % Stringa di avvio del processo B
        % con in ingresso l'informazione elaborata
        avvioProcessoB(path_proc_B, forzamento)
    catch
        disp("[MATLAB] Loop interrotto manualmente\n");
        break; % Esci dal loop se viene generata un'eccezione
    end
end

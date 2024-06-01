% Impostazione dell'algoritmo di machine learning

% Fase di readdestramento della rete e configurazione
% con le nuove immagini inserite nei vari path

%---------> INSERIRE CODICE <---------%


%---------> INSERIMENTO DEL MODELLO <---------%
% In tale caso utilizzo in maniera assoluta alexnet
net = alexnet;


%---------> FASE DI ANALISI DELL'IMMAGINE <---------%

% Caricare la nuova immagine
newImage = imread('carlo.jpg');

% Ridimensionare l'immagine alla dimensione richiesta dalla rete
inputSize = net.Layers(1).InputSize;
resizedImage = imresize(newImage, [inputSize(1) inputSize(2)]);

% Classificare l'immagine
[label, scores] = classify(net, resizedImage);

% Visualizzare la previsione
figure;
imshow(newImage);
title(['Predicted: ' char(label)]);
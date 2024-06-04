load("ReteTrainata\Binnet.mat", "trainedNet");

image_path = "C:\Users\HP\Documents\Prova\S-MA-R-TLOTER_AI\MATLAB\Immagini\giggino.jpg";

%---------> FASE DI ANALISI DELL'IMMAGINE <---------%

% Caricare la nuova immagine
newImage = imread(image_path);

% Ridimensionare l'immagine alla dimensione richiesta dalla rete
inputSize = trainedNet.Layers(1).InputSize;
resizedImage = imresize(newImage, [inputSize(1) inputSize(2)]);

% Classificare l'immagine
[label, scores] = classify(trainedNet, resizedImage);

% Visualizzare la previsione
figure;
imshow(newImage);
title(['Predicted: ' char(label)]);
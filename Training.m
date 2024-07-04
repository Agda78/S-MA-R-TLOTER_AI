% -----> INFO GENERALI <----- %
% Percorso del dataset
datasetPath = 'dataset_path';

% Nome del file in cui sarà salvata la nuova rete
nome_nuova_rete = "Binnet_2.mat";

% -----> DATASET <----- %
% Crea un oggetto imageDatastore
imds = imageDatastore(datasetPath, ...
    'IncludeSubfolders', true, ...
    'LabelSource', 'foldernames');
% Ridimensiona le immagini a 227x227x3
imds.ReadFcn = @(filename)imresize(imread(filename), [227, 227]);

% Suddividi il dataset
[imdsTrain, imdsValidation] = splitEachLabel(imds, 0.8, 'randomized');


% -----> TRAINING PREPARATION <----- %
% Carica AlexNet
net = alexnet;

% Modifica l'ultimo fully connected layer e l'output layer
numClasses = numel(categories(imdsTrain.Labels));
layers = net.Layers;
layers(23) = fullyConnectedLayer(numClasses, 'Name', 'fc', 'WeightLearnRateFactor', 10, 'BiasLearnRateFactor', 10);
layers(25) = classificationLayer('Name', 'output');

% Configura le opzioni di addestramento
options = trainingOptions('sgdm', ...
    'MiniBatchSize', 64, ...
    'MaxEpochs', 10, ...
    'InitialLearnRate', 1e-4, ...
    'ValidationData', imdsValidation, ...
    'ValidationFrequency', 30, ...
    'Verbose', false, ...
    'Plots', 'training-progress');


% -----> TRAINING <----- %
% Addestra la rete
[trainedNet, trainInfo] = trainNetwork(imdsTrain, layers, options);


% -----> STATISTICHE <----- %
% Valuta la rete addestrata
predictedLabels = classify(trainedNet, imdsValidation);
accuracy = mean(predictedLabels == imdsValidation.Labels);
disp(['Validation accuracy: ', num2str(accuracy * 100), '%']);


% -----> TEST VISIVO <----- %

% Numero di immagini casuali da analizzare
numImages = 2;

% Seleziona immagini casuali dal set di validazione
idx = randperm(numel(imdsValidation.Files), numImages);
randomImages = subset(imdsValidation, idx);

% Classifica le immagini selezionate
predictedLabels = classify(trainedNet, randomImages);

% Estrai le etichette reali
trueLabels = randomImages.Labels;

% Visualizza le immagini con le etichette previste e reali
figure;
for i = 1:numImages
    subplot(1, numImages, i);
    img = readimage(randomImages, i);
    imshow(img);
    title({['Predicted: ' char(predictedLabels(i))], ['True: ' char(trueLabels(i))]});
end

% -----> SALVATAGGIO DELLA RETE <----- %
filepath = "path_salvataggio_rete" + nome_nuova_rete;
save(filepath, "trainedNet");
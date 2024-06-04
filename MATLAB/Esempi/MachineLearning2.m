% Impostazione dell'algoritmo di machine learning

% Fase di readdestramento della rete e configurazione
% con le nuove immagini inserite nei vari path

%---------> INSERIRE CODICE <---------%

%random_image_download
% image_path = 'C:\Users\HP\Documents\Prova\S-MA-R-TLOTER_AI\MATLAB\Immagini\giggino.jpg'


% Fase di impostazione del training
imds = imageDatastore('Train','IncludeSubfolders',true,'LabelSource','foldernames');

[imdsTrain, imdsValidation] = splitEachLabel(imds, 0.7, 'randomized');

numTrainImages = numel(imdsTrain.Labels);

% idx = randperm(numTrainImages,5);
% figure
% for i = 1:16
%     subplot(4,4,i)
%     I = readimage(imdsTrain,idx(i));
%     imshow(I)
% end

classNames = categories(imdsTrain.Labels);
numClasses = numel(classNames);

net = alexnet;

analyzeNetwork(net);
inputSize = net.Layers(1).InputSize;

pixelRange = [-30 30];
imageAugmenter = imageDataAugmenter( ...
    'RandXReflection',true, ...
    'RandXTranslation',pixelRange, ...
    'RandYTranslation',pixelRange);
augimdsTrain = augmentedImageDatastore(inputSize(1:2),imdsTrain, ...
    'DataAugmentation',imageAugmenter);

augimdsValidation = augmentedImageDatastore(inputSize(1:2),imdsValidation);
options = trainingOptions("sgdm", ...
    MiniBatchSize=10, ...
    MaxEpochs=6, ...
    Metrics="accuracy", ...
    InitialLearnRate=1e-4, ...
    Shuffle="every-epoch", ...
    ValidationData=augimdsValidation, ...
    ValidationFrequency=3, ...
    Verbose=false, ...
    Plots="training-progress");

net = trainNetwork(imdsTrain,net,"crossentropy",options);

scores = minibatchpredict(net,augimdsValidation);
YPred = scores2label(scores,classNames);

idx = randperm(numel(imdsValidation.Files),2);
figure
for i = 1:4
    subplot(2,2,i)
    I = readimage(imdsValidation,idx(i));
    imshow(I)
    label = YPred(idx(i));
    title(string(label));
end

% %---------> INSERIMENTO DEL MODELLO <---------%
% % In tale caso utilizzo in maniera assoluta alexnet
% net = alexnet;
% 
% 
% %---------> FASE DI ANALISI DELL'IMMAGINE <---------%
% 
% % Caricare la nuova immagine
% newImage = imread(image_path);
% 
% % Ridimensionare l'immagine alla dimensione richiesta dalla rete
% inputSize = net.Layers(1).InputSize;
% resizedImage = imresize(newImage, [inputSize(1) inputSize(2)]);
% 
% % Classificare l'immagine
% [label, scores] = classify(net, resizedImage);
% 
% % Visualizzare la previsione
% figure;
% imshow(newImage);
% title(['Predicted: ' char(label)]);
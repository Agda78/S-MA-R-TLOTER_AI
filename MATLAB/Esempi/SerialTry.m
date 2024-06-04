% Specifica la porta seriale a cui è collegato l'Arduino (es. 'COM3')
port = 'COM13'; % Cambia 'COM3' con la porta appropriata

% Crea un oggetto seriale
arduino = serialport(port, 9600);


% Inizializza un array per memorizzare i dati
data = [];

% Leggi i dati dalla porta seriale
for i = 1:100
    if arduino.BytesAvailable > 0 % Controlla se ci sono dati disponibili
        rawData = fscanf(arduino, '%s'); % Legge i dati come stringa
        value = str2double(rawData); % Converte la stringa in un numero float
        if ~isnan(value) % Controlla se la conversione ha avuto successo
            disp(value); % Visualizza il valore letto
            data = [data, value]; % Aggiunge il valore all'array
        end
    end
    pause(0.1); % Attendi un po' di tempo prima di leggere il prossimo valore
end

% Chiudi la connessione seriale
fclose(arduino);
delete(arduino);
clear arduino;

% Visualizza i dati letti in un grafico
plot(data);
xlabel('Samples');
ylabel('Sensor Value');
title('Arduino Sensor Data');

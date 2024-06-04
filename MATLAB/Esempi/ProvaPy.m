com_port = 'COM13';
baud_rate = 9600;

% Esempio di utilizzo
disp('Invio comando ON:');
response = control_arduino('ON', com_port, baud_rate);
disp(response);

disp('Invio comando OFF:');
response = control_arduino('OFF', com_port, baud_rate);
disp(response);

disp('Richiesta numero casuale:');
response = control_arduino('GET',com_port, baud_rate);
disp(['Numero casuale ricevuto: ', response]);

response = str2num(response)

# s7_Python_MQTT_Nodered
Aplicação em Python coleta informações do CLP, envia dado para o Broker HiveMQ em Nuvem. Nodered assina o endereço e gera um Dashboard.

Realiza a leitura de um enderço no CLP, quando o endereço muda de valor, envia para o Broker HiveMQ em nuvem. Utilzando o Node-red, coletamos as informações e geramos um dashboard com o valor coletado;

Para o exemplo, foi utilizado o Python 3.8.1; Bibliotecas: Snap7 e Paho;

O CLP Utilizado foi o S71500 da Siemens.

Deixamos o código em Python de exemplo, o Flow do node-red e a aplicação do CLP;

Autor: Douglas Silva.

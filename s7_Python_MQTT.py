#Importação das bibliotecas
import time
from paho.mqtt import client as mqtt_client
import snap7
from snap7.util import*

#Configuração do SNAP7 e tenta a conexão com CLP. IP, Rack, Slot
clients7 = snap7.client.Client()
clients7.connect('192.168.0.201', 0, 1)

#Configuração dos dados MQTT
broker = "d15bfd43dad24009a93b08057369e0e1.s1.eu.hivemq.cloud"
port = 8883
topic = "S7/Python/MQTT"
client_id = 'pythonS7'
username = 'seu usuario do broker vai aqui'
password = 'sua senha do Broker vai aqui'

#Conecta com o Broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Broker conectado")
        else:
            print("Erro de conexão %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.tls_set(tls_version=mqtt_client.ssl.PROTOCOL_TLS)
    client.connect(broker, port)
    return client

#Carrega variável do CLP, verifica se ocorreu mudança. Se sim publica o dado no Broker.
def publish(client):
    var01Anterior=0
    while True:
        #Vai executar a cada 5 segundos
        time.sleep(5)

        #Leitura de 2Bytes(uma word do DB1 e escreve o valor 10)
        comm=clients7.get_connected()
        if comm:
            #Leitura CLP
            data = clients7.db_read(1, 0, 2)
            #converte buffer para int
            data=get_int(data,0)
            print("var01:", data) 

            if data != var01Anterior:  
                #Publica do dado lido do CLP no broker
                result = client.publish(topic, data)

                # Verifica se foi publicado
                status = result[0]
                if status == 0:
                    print(f"Publicado {data} to {topic}", )
                else:
                    print(f"Falha na publicação {data} to {topic}")

            #Variável recebe o novo valor
            var01Anterior=data
        else:
            print("erro na leitura do CLP")


client = connect_mqtt()
client.loop_start()
publish(client)


# FastAPI MQTT Restaurant Service

Este proyecto implementa una API usando FastAPI que simula un sistema de pedidos de hamburguesas y bebidas. Los pedidos se procesan de forma asíncrona a través de MQTT, con un "trabajador" separado para cada tipo de pedido.

## Funcionalidades

- **Pedidos de Hamburguesas:** Se puede realizar un pedido de una cantidad específica de hamburguesas a través del endpoint `/order/burgers/{number_of_burgers}`, que se publicará en el tópico `burger_orders` de MQTT.
- **Pedidos de Bebidas:** Se puede realizar un pedido de una bebida específica a través del endpoint `/order/drinks/{drink_type}`, que se publicará en el tópico `drink_orders` de MQTT.

Cada tipo de pedido es procesado por un "trabajador" que escucha el tópico correspondiente en MQTT.

## Prueba Funcionamiento 
<img src="https://github.com/JonathanArroyaveGonzalez/ConcurrenciaYParalelismoWeb/blob/main/PruebaFuncionamiento.png?raw=true" alt="Prueba de funcionamiento" width="700px">

## Requisitos

- Python 
- FastAPI
[- MQTT Explorer](https://mqtt-explorer.com/)
- Uvicorn
[- Servidor MQTT Mosquitto ](https://mosquitto.org/download/)

## Instalación

1. Clona el repositorio.
   ```bash
   git clone https://github.com/JonathanArroyaveGonzalez/ConcurrenciaYParalelismoWeb.git
2. Iniciar el servidor.
   ```bash
   uvicorn 13_burger_server_mqtt:app --reload
3. Realizar peticiones al servidor con los tipos de clientes.
   ```bash
   python 13_burger_client_mqtt_sync.py
   python 13_burger_client_mqtt.py

# FastAPI MQTT Restaurant Service

Este proyecto implementa una API usando FastAPI que simula un sistema de pedidos de hamburguesas y bebidas. Los pedidos se procesan de forma asíncrona a través de MQTT, con un "trabajador" separado para cada tipo de pedido.

## Funcionalidades

- **Pedidos de Hamburguesas:** Se puede realizar un pedido de una cantidad específica de hamburguesas a través del endpoint `/order/burgers/{number_of_burgers}`, que se publicará en el tópico `burger_orders` de MQTT.
- **Pedidos de Bebidas:** Se puede realizar un pedido de una bebida específica a través del endpoint `/order/drinks/{drink_type}`, que se publicará en el tópico `drink_orders` de MQTT.

Cada tipo de pedido es procesado por un "trabajador" que escucha el tópico correspondiente en MQTT.

## Prueba Funcionamiento 
![Prueba](ubicacion_de_la_imagen)

## Requisitos

- Python 3.x
- FastAPI
- Paho MQTT
- Uvicorn
- Servidor MQTT (como Mosquitto)

## Instalación

1. Clona el repositorio.
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

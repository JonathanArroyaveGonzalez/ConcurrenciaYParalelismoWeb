from fastapi import FastAPI
import threading
import time
import paho.mqtt.client as mqtt

app = FastAPI()

# Configurar el cliente MQTT para RabbitMQ (conectado en localhost)
mqtt_client = mqtt.Client()

# Trabajador que procesa las hamburguesas al recibir mensajes de MQTT
def burger_worker():
    def on_message(client, userdata, message):
        # Procesar el mensaje recibido desde MQTT (cantidad de hamburguesas)
        num_burgers = int(message.payload.decode('utf-8'))
        print(f"Preparando {num_burgers} hamburguesa(s)...")
        time.sleep(4)  # Simula el tiempo de preparación de la hamburguesa
        print(f"{num_burgers} hamburguesa(s) preparada(s)")

    mqtt_client.message_callback_add("burger_orders", on_message)
    mqtt_client.subscribe("burger_orders")  # Suscribirse al tópico 'burger_orders'

# Trabajador que procesa las bebidas al recibir mensajes de MQTT
def drink_worker():
    def on_message(client, userdata, message):
        # Procesar el mensaje recibido desde MQTT (tipo de bebida)
        drink_type = message.payload.decode('utf-8')
        print(f"Preparando bebida: {drink_type}...")
        time.sleep(2)  # Simula el tiempo de preparación de la bebida
        print(f"Bebida {drink_type} preparada")

    mqtt_client.message_callback_add("drink_orders", on_message)
    mqtt_client.subscribe("drink_orders")  # Suscribirse al tópico 'drink_orders'

# Conectar y mantener MQTT activo en un hilo separado
def start_mqtt():
    mqtt_client.connect("localhost", 1883, 60)  # Conectar a RabbitMQ en el puerto MQTT 1883
    mqtt_client.loop_forever()  # Mantener la conexión MQTT abierta

# Iniciar los trabajadores de hamburguesas y bebidas en hilos para escuchar mensajes MQTT
threading.Thread(target=burger_worker, daemon=True).start()
threading.Thread(target=drink_worker, daemon=True).start()
threading.Thread(target=start_mqtt, daemon=True).start()

# Endpoint para ordenar hamburguesas (publica en el tópico 'burger_orders')
@app.get("/order/burgers/{number_of_burgers}")
def order_burgers(number_of_burgers: int):
    # Publicar el pedido de hamburguesas en el tópico 'burger_orders'
    mqtt_client.publish("burger_orders", str(number_of_burgers))
    return {"message": f"Tu pedido de {number_of_burgers} hamburguesa(s) está siendo preparado"}

# Endpoint para ordenar bebidas (publica en el tópico 'drink_orders')
@app.get("/order/drinks/{drink_type}")
def order_drinks(drink_type: str):
    # Publicar el pedido de bebida en el tópico 'drink_orders'
    mqtt_client.publish("drink_orders", drink_type)
    return {"message": f"Tu pedido de bebida {drink_type} está siendo preparado"}

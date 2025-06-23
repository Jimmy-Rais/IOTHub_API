from fastapi_mqtt import FastMQTT, MQTTConfig
from . import config
from . import topics
from app.crud_services import device_state
import asyncio
#Here,we handle all the connectivity operations on the mqtt broker
BROKER_HOST = config.settings.broker_url
BROKER_PORT = int( config.settings.broker_port)
USERNAME=  config.settings.broker_username
PASSWORD= config.settings.broker_password

mqtt_config = MQTTConfig(
    host=BROKER_HOST,
    port=BROKER_PORT,
    keepalive=60,
    username=USERNAME,
    password=PASSWORD,
    reconnect_retries=3,
    reconnect_delay=2,
    ssl=True
)
mqtt = FastMQTT(config=mqtt_config)
@mqtt.on_connect()
def handle_connect(client, flags, rc, properties):
    print("MQTT connected with result code:", rc)
    client.subscribe(topics.device1_state_topic)
    client.subscribe(topics.device1_data_topic)
    client.subscribe(topics.device2_state_topic)
    client.subscribe(topics.device2_data_topic)
@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("MQTT disconnected")
# Handle incoming messages
@mqtt.on_message()
async def handle_message(client, topic, payload, qos, properties):
    #Handles incoming state commands from the user
    ''''''
    if (topic==topics.device1_state_topic or topic==topics.device2_state_topic):
       state= payload.decode()
       new_payload = {"state":state}
       print(new_payload)
       #crud_service handler for specific iot device according to the topic
       handler=topics.state_topic_handler.get(topic)
       asyncio.create_task(handler(new_payload))
   
    #Handles incoming data from the iot device
    elif (topic==topics.device1_data_topic or topic==topics.device2_data_topic):
       data= payload.decode()
       new_payload = {"data":data}
       #crud_service handler for specific iot device according to the topic
       handler=topics.data_topic_handler.get(topic)
       asyncio.create_task(handler(new_payload))
       print("suceess")
    else:
        return "Unmatched topic"
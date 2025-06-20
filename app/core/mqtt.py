from fastapi_mqtt import FastMQTT, MQTTConfig
from . import config
from . import topics
from app.crud_services import device_service
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
    client.subscribe(topics.device1_topic)
    client.subscribe(topics.device2_topic)
    print(f"Subscribed to topics ")
@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("MQTT disconnected")
# Handle incoming messages
@mqtt.on_message()
async def handle_message(client, topic, payload, qos, properties):
   try:
       data= payload.decode()
        #Select the appropriate crud service for each device    
       #handler=topics.topic_router.get(topic)
       print(data)
       #await handler(data)
   except Exception as e:
        print(f"Error decoding message: {e}")
  
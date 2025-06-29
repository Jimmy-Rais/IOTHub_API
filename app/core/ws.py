#Websockets integration
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
import threading
import json
from app.crud_services import device1_latest,device2_latest
# Sensor data db calls
SIMULATED_DB = [
    {"device_id": "dev1", "data":device1_latest()},
      {"device_id": "dev2", "data":device2_latest()},
]

# WebSocket Connection Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_personal_json(self, message: dict, websocket: WebSocket):
        await websocket.send_text(json.dumps(message))

    async def broadcast_json(self, message: dict, allowed_clients: list[WebSocket]):
        for connection in allowed_clients:
            try:
                await connection.send_text(json.dumps(message))
            except:
                self.disconnect(connection)

manager = ConnectionManager()

# Map WebSocket clients to their subscribed device_ids
client_subscriptions: dict[WebSocket, list[str]] = {}

# Get latest data for a list of device_ids
def get_latest_sensor_data(device_ids: list[str]):
    return [entry for entry in SIMULATED_DB if entry["device_id"] in device_ids]

# WebSocket route with client_id and subscription handling
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)

    try:
        # Step 1: Get subscription request from client
        init_msg = await websocket.receive_json()
        subscribed_devices = init_msg.get("subscribe", [])
        client_subscriptions[websocket] = subscribed_devices

        # Step 2: Send the latest DB data for subscribed devices
        latest_data = get_latest_sensor_data(subscribed_devices)
        for row in latest_data:
            await manager.send_personal_json({
                "type": "initial",
                "device_id": row["device_id"],
                "sensor": row["sensor"],
                "value": row["value"]
            }, websocket)

        # Step 3: Keep the connection alive
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        client_subscriptions.pop(websocket, None)

# Handle MQTT messages and route to the right WebSocket clients
def on_mqtt_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        topic_parts = msg.topic.split("/")  # Example: sensors/temp/dev1
        sensor_type = topic_parts[1]
        device_id = topic_parts[2]

        data = {
            "type": "update",
            "device_id": device_id,
            "sensor": sensor_type,
            "value": payload["value"]  # assuming JSON format: {"value": ...}
        }

        # Send to only relevant WebSocket clients
        allowed_clients = [
            ws for ws, subs in client_subscriptions.items()
            if device_id in subs
        ]

        asyncio.run(manager.broadcast_json(data, allowed_clients))

    except Exception as e:
        print("MQTT message error:", e)

# Connect to MQTT broker and subscribe
def start_mqtt():
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = on_mqtt_message
    mqtt_client.connect("broker.hivemq.com", 1883)
    mqtt_client.subscribe("sensors/+/+")
    mqtt_client.loop_forever()

# Start MQTT in background thread
threading.Thread(target=start_mqtt, daemon=True).start()

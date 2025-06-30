#Websockets integration
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
import threading
import json
from app.crud_services.device_data import device1_latest,device2_latest
# Sensor data db calls
SIMULATED_DB = [
    {"device_id": "device1/data", "data":device1_latest()},
      {"device_id": "device2/data", "data":device2_latest()},
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


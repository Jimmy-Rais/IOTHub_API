from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from .. import schemas
from app.utils import auth
from app.core import ws
#End point for signing up  Loging in users
router=APIRouter(
    prefix="/ws",
    tags=["WEB SOCKET ENDPOINT"]
)
# WebSocket route with client_id and subscription handling
@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await ws.manager.connect(websocket)

    try:
        # Step 1: Get subscription request from client
        init_msg = await websocket.receive_json()
        subscribed_devices = init_msg.get("subscribe", [])
        ws.lient_subscriptions[websocket] = subscribed_devices

        # Step 2: Send the latest DB data for subscribed devices
        latest_data = ws.get_latest_sensor_data(subscribed_devices)
        for row in latest_data:
            await ws.manager.send_personal_json({
                "type": "initial",
                "value": row["data"]
            }, websocket)

        # Step 3: Keep the connection alive
        while True:
            await websocket.receive_text()

    except ws.WebSocketDisconnect:
        ws.manager.disconnect(websocket)
        ws.client_subscriptions.pop(websocket, None)
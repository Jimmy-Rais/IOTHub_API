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
async def websocket_endpoint(websocket: WebSocket,client_id:int):
      await ws.manager.connect(websocket)
      try:
            while True:
                  data=await websocket.receive_text()
                  await ws.manager.send_personal_message(data,websocket)
                  await ws.manager.broadcast(f"client {client_id} says {data}")
      except WebSocketDisconnect:
            ws.manager.disconnect(websocket)
            ws.manager.broadcast(f"client {client_id} left")
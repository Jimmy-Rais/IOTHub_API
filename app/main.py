from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api_routers import actuators,sensors,commands,users,websocket
from app.core.mqtt import mqtt

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(sensors.router)
app.include_router(actuators.router)
app.include_router(commands.router)
app.include_router(users.router)
app.include_router(websocket.router)
mqtt.init_app(app)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api_routers import devices, commands,users
from app.core.mqtt import mqtt

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(devices.router)
app.include_router(commands.router)
app.include_router(users.router)
mqtt.init_app(app)

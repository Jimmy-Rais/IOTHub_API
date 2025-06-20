'''
This endpoint is used to send commands to the iot devices through the MQTT broker,
each device is associated to a specific top and is subscribed to it.
'''
from fastapi import APIRouter,HTTPException
from app.core.mqtt import mqtt
from .. import schemas
from app.core import topics
from app.crud_services import device_service
router=APIRouter(
    prefix="/command",
    tags=["SEND COMMANDS TO THE MQTT BROKER'S TOPICS"]
)
#Send commands to the iot device 2
#Send commands to the iot device 1
@router.post("/device1")
async def publish_command(payload:schemas.Command):
    try:
        mqtt.publish(topics.device1_topic, payload.data)
        return {"status": "success", "topic":topics.device1_topic, "message": payload.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {e}")
#Send commands to the iot device 2
@router.post("/device2")
async def publish_command(payload:schemas.Command):
    try:
        mqtt.publish(topics.device2_topic, payload.data)
        return {"status": "success", "topic":topics.device2_topic, "message": payload.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {e}")
#We can add as may devices as required
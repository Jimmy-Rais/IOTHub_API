'''
This endpoint is used to send commands to the iot devices through the MQTT broker,
each device is associated to a specific topic To which it is subscribed.
Since commands need to be modified and not created(for example,on/off,changing the 
motor's speed,etc.), we will be using patch requests.
)
'''
from fastapi import APIRouter,HTTPException
from app.core.mqtt import mqtt
from .. import schemas
from app.core import topics
from app.utils import auth
from fastapi import Depends
router=APIRouter(
    prefix="/command",
    tags=["SEND COMMANDS TO THE MQTT BROKER'S TOPICS"]
)
#Only authenticated users can access these endpoints
#Endpoint to Send State update commands to the iot device 1
@router.patch("/device1/state/update")
async def device1_state(payload:schemas.Command,user=Depends(auth.verify_token)):
    #print("Recievided  via post",payload.data)
    try:
        mqtt.publish(topics.device1_state_topic, payload.state)
        return {"status": "success", "topic":topics.device1_state_topic, "message": payload.state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {e}")
#Endpoint to Send State update commands to the iot device 2
@router.patch("/device2/state/update")
async def device2_state(payload:schemas.Command):
    try:
        mqtt.publish(topics.device2_state_topic, payload.state)
        return {"status": "success", "topic":topics.device2_state_topic, "message": payload.state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {e}")
#We can add as may devices as required

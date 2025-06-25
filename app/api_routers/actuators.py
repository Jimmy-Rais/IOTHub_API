'''
This end point retrieves actuators states stored in the database(supabase),
Actuators can be viewed as components of the IOT device that recieve commands from the user
and translate
'''
from fastapi import APIRouter,HTTPException,Depends
from app.core.mqtt import mqtt
from .. import schemas
from app.core import topics
from app.crud_services import device_data,device_state
from app.utils import auth
router=APIRouter(
    prefix="/actuators",
    tags=["RETRIEVE ACTUATORS STATES FROM THE DATABASE"]
)
#Only authenticated users can access these endpoints
#Retrieve device1 state from the db
@router.get('/state/device1')
def get_state(user=Depends(auth.verify_token)):
   return device_state.device1_read_state()
#Retrieve device2 state from the db
@router.get('/state/device2')
def get_state(user=Depends(auth.verify_token)):
   return device_state.device2_read_state()
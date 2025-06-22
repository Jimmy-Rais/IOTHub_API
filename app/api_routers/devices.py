from fastapi import APIRouter,HTTPException
from app.core.mqtt import mqtt
from .. import schemas
from app.core import topics
from app.crud_services import device_data,device_state
router=APIRouter(
    prefix="/device",
    tags=["RETRIEVE IOT DEVICES DATA FROM THE DATABASE"]
)
'''
This end point retrieves iot devices data stored in the database(supabase)
'''
#Retrieve device1 state from the db
@router.get('/state/device1')
def get_state():
   return device_state.device1_read_state()
#Retrieve device2 state from the db
@router.get('/state/device2')
def get_state():
   return device_state.device2_read_state()
#Retrieve the latest device 1 data
#@router.get('/data/latest/device1')
#def get_latest_data():
 #  return device_state.device1_read_state()
#Retrieve the latest device 2 data
#Retrieve all device1 data
#Retrieve all device2 data
    


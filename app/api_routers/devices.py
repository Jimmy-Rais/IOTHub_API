'''
This end point retrieves iot devices data & state stored in the database(supabase)
'''
from fastapi import APIRouter,HTTPException,Depends
from app.core.mqtt import mqtt
from .. import schemas
from app.core import topics
from app.crud_services import device_data,device_state
from app.utils import auth
router=APIRouter(
    prefix="/device",
    tags=["RETRIEVE IOT DEVICES DATA & STATE FROM THE DATABASE"]
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
#Retrieve the latest device 1 data
@router.get('/data/device1/latest')
def get_latest_data_device1(user=Depends(auth.verify_token)):
   return device_data.device1_latest()
#Retrieve the latest device2 data
@router.get('/data/device2/latest')
def get_latest_data_device2(user=Depends(auth.verify_token)):
   return device_data.device2_latest()
#Retrieve all device1 data
@router.get('/data/device1/all')
def get_device1_all(user=Depends(auth.verify_token)):
   return device_data.device1_read()
#Retrieve all device2 data
@router.get('/data/device2/all')
def get_device2_all(user=Depends(auth.verify_token)):
   return device_data.device2_read()


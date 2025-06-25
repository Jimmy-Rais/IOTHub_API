'''
This end point retrieves sensors data stored in the database(supabase)
'''
from fastapi import APIRouter,HTTPException,Depends
from app.core.mqtt import mqtt
from .. import schemas
from app.core import topics
from app.crud_services import device_data,device_state
from app.utils import auth
router=APIRouter(
    prefix="/sensors",
    tags=["RETRIEVE SENSORS DATA FROM THE DATABASE"]
)
#Retrieve the latest device 1 data
@router.get('/data/sensor1/latest')
def get_latest_data_device1(user=Depends(auth.verify_token)):
   return device_data.device1_latest()
#Retrieve the latest device2 data
@router.get('/data/sensor2/latest')
def get_latest_data_device2(user=Depends(auth.verify_token)):
   return device_data.device2_latest()
#Retrieve all device1 data
@router.get('/data/sensor1/all')
def get_device1_all(user=Depends(auth.verify_token)):
   return device_data.device1_read()
#Retrieve all device2 data
@router.get('/data/sensor2/all')
def get_device2_all(user=Depends(auth.verify_token)):
   return device_data.device2_read()
#The number of sensors can be expanded according to the project needs
'''
Here, the data sent to the MQTT Broker by the iot devices is stored
 in supabase(our remote database),and the user can retrieve that data.
'''
from .. import database
from fastapi import HTTPException
#from app.core.mqtt import mqtt
#from app.core.topics import device1_topic,device2_topic
db=database.supabase
#iot_device1 add data
async def device1_add(data):
    try:
        db.table("iot_device1_data").insert(data).execute()
    except Exception as e:
        return e 
#iot_device2 add data
async def device2_add(data):
    try:
        db.table("iot_device2_data").insert(data).execute()
    except Exception as e:
        return e 
#iot_device1 read data(all)
def device1_read():
    response=db.table("iot_device1_data").select('data','created_at').execute()
    return response.data
#iot_device2 read data(all)
def device2_read():
    response=db.table("iot_device2_data").select('data','created_at').execute()
    return response.data
#iot_device1_read_latest data
def device1_latest():
    response=db.table('latest_data_device1').select('data','created_at').execute()
    return response.data[0]
#iot_device2_read_latest data
def device2_latest():
    response=db.table('latest_data_device2').select('data','created_at').execute()
    return response.data[0]
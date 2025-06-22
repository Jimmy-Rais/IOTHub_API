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
#iot_device1 read data
def device1_read():
    data=db.table("iot_device1_data").select('data').execute()
    return data
#iot_device2 read data
async def device2_read():
    data=db.table("iot_device2_data").insert(data).execute()
    return data

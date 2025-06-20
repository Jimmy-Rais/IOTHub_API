'''
Here, the data sent to the MQTT Broker by the iot devices is stored
 in supabase(our remote database)
'''
from .. import database
from fastapi import HTTPException
db=database.supabase
#iot_device1 add data
async def device1_add(data):
    try:
        db.table("iot_device1").insert(data).execute()
    except Exception as e:
        return e 
#iot_device1 read data
def device1_read():
    data=db.table("iot_device1").select('data').execute()
    return data
#iot_device2 add data
def device2_add(data):
    db.table("iot_device2").insert(data).execute()
#iot_device2 read data
def device2_read():
    data=db.table("iot_device2").select('data').execute()
    return data

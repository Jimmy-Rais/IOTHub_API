'''
Here We handle db operations(update and retrieve) on iot devices states
'''
from .. import database
from fastapi import HTTPException
db=database.supabase
#Update the state of iot_device1
async def device1_state(state):
    try:
       response=db.table("iot_device1_state").update(state).eq('id',1).execute()
       return response
    except Exception as e:
        return e
#Read the state of iot_device1
def device1_read_state():
    response=db.table('iot_device1_state').select('state','last_modified').execute()
    return response.data[0]
#iot_device2 update state
async def device2_state(state):
    try:
       response=db.table("iot_device2_state").update(state).eq('id',1).execute()
       return response
    except Exception as e:
        return e
#iot_device2 read state
def device2_read_state():
    response=db.table('iot_device2_state').select('state','last_modified').execute()
    return response.data[0]
#iot_device1_latest_data
def device1_latest():
    response=db.table('iot_device1_data').select('data').eq().execute
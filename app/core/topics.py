'''
In this file,we keep the topic names for each iot device.
Intuitively, topics can be viewed as tables or collections in a database
'''
from app.crud_services import device_state,device_data
device1_data_topic="hub/device1/data"
device1_state_topic="hub/device1/state"
device2_data_topic="hub/device2/data"
device2_state_topic="hub/device2/state"
'''
Here we create a dictionary that associates each topic name to the 
corresponding db_service for updating the device state
'''
#
state_topic_handler = {
        device1_state_topic:device_state.device1_state,
        device2_state_topic:device_state.device2_state,

    }
data_topic_handler = {
        device1_data_topic:device_data.device1_add,
        device2_data_topic:device_data.device2_add,

    }

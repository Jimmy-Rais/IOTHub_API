'''
In this file,we keep the topic names for each iot device.
Intuitively, topics can be viewed as tables or collections in a database
'''
from app.crud_services import device_service 
device1_topic="hub/device1"
device2_topic="hub/device2"
#Here we create a dictionary that associates each topic name to the corresponding crud_service
topic_router = {
        device1_topic:device_service.device1_add,
        device2_topic:device_service.device1_add,

    }

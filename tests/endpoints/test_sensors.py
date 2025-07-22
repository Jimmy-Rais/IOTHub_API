from . import test_users
client=test_users.client
#Sensor
def test_sensor1_latest():
    response=client('sensors/data/sensor1/latest')
    assert response.status==200
def test_sensor1_all():
    response=client('sensors/data/sensor1/all')
    assert response.status==200

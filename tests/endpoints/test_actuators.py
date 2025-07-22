from . import test_users
client=test_users.client
#Test actuators status
def test_actuator_1():
    response=client.get('actuators/state/device1')
    assert response.status==200
    #Check the status code
def test_actuato_2():
    response=client.get('actuators/state/device2')
    assert response.status==200
from . import test_users
client=test_users.client
#Test actuators status
def test_actuators():
    response=client.get('')
    #Check the status code
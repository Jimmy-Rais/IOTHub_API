from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
#Sensor
def test_sensor1():
     #response=client
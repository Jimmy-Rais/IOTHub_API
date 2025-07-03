from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
#Actuator
def test_actuator1():
     #response=client
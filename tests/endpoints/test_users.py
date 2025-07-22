from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
#Signup
#def test_signup():
 #    response=client
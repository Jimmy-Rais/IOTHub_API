from pydantic import BaseModel
class Command(BaseModel):
    state:str
class Data(BaseModel):
    data:str
class UserSignup(BaseModel):
    email:str
    password:str
class SigninOtp(BaseModel):
    email:str
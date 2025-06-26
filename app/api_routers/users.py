from fastapi import APIRouter
from .. import schemas
from app.utils import auth
#End point for signing up & Loging in users
router=APIRouter(
    prefix="/user",
    tags=["USER MANAGEMENT ENDPOINTS"]
)
#Signup
@router.post('/signup')
def signup(credentials:schemas.UserSignup):
    return auth.signup(credentials)
#Login
@router.post("/signin")
def signin(credentials:schemas.UserSignup):
    return auth.signin(credentials)
#Login with otp(magic link)
@router.post("/signin/otp")
def otp_signin(email:str):
    return auth.login_otp(email)
#Forgot password
#Refresh token
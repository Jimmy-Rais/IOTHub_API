#Handle user authentification(jwt)
from .. import database
from fastapi import HTTPException, Header
from supabase import create_client, Client
import jwt
#Create a new user with Email and Password
def signup(credentials):
    database.supabase.auth.sign_up({
        "email":credentials.email,
        "password":credentials.password
    })
    return "A verification link has been sent to your email"
#Log in user
def signin(credentials):
    try:
       session=database.supabase.auth.sign_in_with_password({
        "email":credentials.email,
        "password":credentials.password
       })
       access_token = session.session.access_token
       return access_token
    except:
        raise HTTPException(status_code=403,detail="Login failed,verify credentials")
   
#Signing out
def signout():
    database.supabase.auth.signout()
#Jwt auth
def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.replace("Bearer ", "")

    try:
        user = database.supabase.auth.get_user(token).user
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
#Login with email otp(magic link)
def login_otp(email):
    response = database.supabase.auth.sign_in_with_otp({
  'email':email,
  'options': {
    'should_create_user': False,
  },
})

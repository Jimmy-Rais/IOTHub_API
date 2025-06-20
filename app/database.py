#INITIALIZE SUPABASE CLIENT
from app.core import config
from supabase import create_client, Client
SUPABASE_URL_CLIENT =config.settings.supabase_url
SUPABASE_KEY =config.settings.supabase_api_key
#Initialize a db client
supabase: Client = create_client(SUPABASE_URL_CLIENT, SUPABASE_KEY)
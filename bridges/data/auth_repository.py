import os
from bridges.app.schema import Signup
from supabase import create_client, Client


def signup_with_email(signup: Signup):
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
    return supabase.auth.sign_up(
        {
            'email': signup.email,
            'password': signup.password,
        }
    )

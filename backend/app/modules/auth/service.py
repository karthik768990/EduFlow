import requests
from app.core.config import SUPABASE_URL, SUPABASE_KEY

class AuthService:
    @staticmethod
    def verify_supabase_token(token: str):
        headers = {
            "Authorization": f"Bearer {token}",
            "apikey": SUPABASE_KEY
        }
        response = requests.get(
            f"{SUPABASE_URL}/auth/v1/user",
            headers=headers
        )
        if response.status_code != 200:
            raise ValueError("Invalid Supabase token")
        return response.json()

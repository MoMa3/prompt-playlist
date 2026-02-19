import requests
from definitions import client_id, client_secret


class SpotifyClient:
    # singleton
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.API_BASE = "https://api.spotify.com/v1"
        self.token = None

    def get_token():
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data=data,
            headers=headers
        )
        print(response.json())
        return response.json()

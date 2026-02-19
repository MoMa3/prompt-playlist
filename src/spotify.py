import spotipy
from definitions import client_id, client_secret
import pandas as pd

class SpotifyClient:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.sp = None

    def connect_app(self):
        if self.sp is None:
            self.sp = spotipy.Spotify(
                auth_manager=spotipy.SpotifyOAuth(
                    client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri="http://127.0.0.1:5000/callback",
                    scope="playlist-read-private playlist-read-collaborative"
                )
            )
        return self.sp

    def search_track(self, query, limit=5):
        sp = self.connect_app()
        res = sp.search(q=query, type="playlist", limit=limit)
        print(res["playlists"]["items"][0].keys())
        return [
            {
                "name": t["name"],
                "owner": t["owner"]["display_name"],
                "id": t["id"],
            }
            for t in res["playlists"]["items"]
        ]

    def get_all_playlist_tracks(self, playlist_id="34Zsyg0s3V6anrBD6SENCZ"):
        sp = self.connect_app()
        results = sp._get(
            f"playlists/{playlist_id}/items",
            limit=100,
            offset=0,
            fields="items(track(id,name,artists(id,name),album(name),popularity,explicit)),next",
            market=None,
            additional_types=",".join(("track", "episode"))
        )
        print(results.keys(), flush=True)
        tracks = results["items"]
        while results["next"]:
            results = sp.next(results)
            tracks.extend(results["items"])

        for item in tracks:
            print(item["item"].keys())
            # track = item["item"]
            # if track:
            #     print(track["artists"][0]["name"], "-", track["name"])
        df = pd.DataFrame(tracks)
        print(df)
        return tracks

    def get_playlist(self, playlist_id="34Zsyg0s3V6anrBD6SENCZ"):
        sp = self.connect_app()
        return sp.playlist(playlist_id)

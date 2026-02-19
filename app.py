from src.spotify import SpotifyClient


spotify_service = SpotifyClient()
a = spotify_service.get_playlist()
print(len(a["items"]["items"]))

# a = spotify_service.get_all_playlist_tracks()
# for i in a:
#     print(i)
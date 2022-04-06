import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"

sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))

# playlists = sp.current_user_playlists()
# for i in playlists['items']:
#     if i['name'] == "r/listentothis":
#         PLAYLIST_ID =  i['id']
PLAYLIST_ID = "1reCDNh1Rc5Vcml2c9c16g"
PLAYLIST_TO_ADD = "6MkYxXCiyCfoI5Amx7ogEb"
# print(sp.playlist_items(PLAYLIST_ID)['items'][10]['added_at'])
# def get_playlist_tracks(playlist_id):
#     results = sp.playlist_tracks(playlist_id, offset=8000, limit = 2)
#     tracks = results['items']
#     while results['next']:
#         results = sp.next(results)
#         tracks.extend(results['items'])
#     return tracks


toadd = []
print()

result = sp.playlist_tracks(PLAYLIST_ID, offset=8500, limit = 100)
for j in result['items']:
    toadd.append(j['track']['id'])
sp.playlist_add_items(PLAYLIST_TO_ADD, items=toadd)

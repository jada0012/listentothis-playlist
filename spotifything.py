import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz


CLIENT_ID = "84526e7160d446198f89e16866f1fda1"
CLIENT_SECRET = "a533c162b74945ccb1b878ff87e9f0bf"
SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"

sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://example.com", scope = SCOPE))
#sp.user_playlist_create(user='5kbehkqoyiok15qrj7uxo55d4', name='Test!', public=True, collaborative=False, description="testing out spotipy")
# playlists = sp.current_user_playlists()
# for i in playlists['items']:
#     if i['name'] == "Test!":
#         PLAYLIST_ID =  i['id']
    


# # results = sp.current_user_recently_played()

# # for i in results['items']:
# #     print(f"{i['track']['name']} by {i['track']['artists'][0]['name']}")
# track_id = []
# results = sp.search(q="track:" + "king for a day", type='track')
# # for i in results['artists']['items']:
# #     print(f"{i['name']}, {i['genres']}, {i['popularity']}")
# for num, i in enumerate(results['tracks']['items']):
#     titleArtist  = i['name']+ '--' + i['artists'][0]['name']
    
    
#     if fuzz.partial_ratio('king for a day -- battle beast', titleArtist) > 70:
#         print(f"{num}, {titleArtist}, {fuzz.partial_ratio('king for a day -- battle beast', titleArtist)}")
#         track_id.append(i['id'])
# print(track_id)
# sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=track_id)
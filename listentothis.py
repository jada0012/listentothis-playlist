import os 
import praw
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz
import schedule
from dotenv import load_dotenv
load_dotenv()



SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"

sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))
#sp.user_playlist_create(user='5kbehkqoyiok15qrj7uxo55d4', name='Listen to This 2.0', public=True, collaborative=False, description="testing out spotipy")

playlists = sp.current_user_playlists()
for i in playlists['items']:
    if i['name'] == "Listen to This 2.0":
        PLAYLIST_ID =  i['id']

inplaylist = []
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

for track in get_playlist_tracks(PLAYLIST_ID):
    trackid  = track['track']['id']
    inplaylist.append(trackid)

with open('ids.txt', 'a') as f:
    for track in inplaylist:
        f.write(track)
        f.write('\n')
# reddit = praw.Reddit(
#     client_id = os.getenv('REDDIT_CLIENT_ID'),
#     client_secret = os.getenv('REDDIT_CLIENT_SECRET'),
#     user_agent = os.getenv('USER_AGENT'),
# )
# def addSongs():
#     subreddit = reddit.subreddit("listentothis")
#     track_ids = []
#     song_titles_toSearch = []
#     similarity = 70
#     anotherlist = []
#     missed = []

#     for submission in subreddit.top("day"):
#         x = submission.title.index('[')
#         song = submission.title[:x].lower()
#         if song :
#             song_titles_toSearch.append(song)



        
#     for title in song_titles_toSearch:

#         if "--" in title:
#             title = title.split('--')
#         elif "- -" in title:
#             title = title.split('- -')
        
#         elif '—' in title:
#             title = title.split('—')
#         elif '–' in title:
#             title = title.split('–')
#         elif '-' in title:
#             title = title.split('-')
    

#         results = sp.search(q="track:" + title[1] + title[0], type="track")
#         if len(results['tracks']['items']) != 0:
#             for result in results['tracks']['items']:
#                 resultName  = result['name'].lower()
#                 resultArtists =  result['artists'][0]['name'].lower()
#                 titleArtist = resultName + '--' + resultArtists

#                 if (fuzz.partial_ratio(resultName, title[1]) >= similarity) and (fuzz.partial_ratio(resultArtists, title[0])) >= similarity:
#                     if not result['id'] in anotherlist:
#                         anotherlist.append(result['id'])
#                         break
#                 else:
#                     print(f"the score for title similarity between {resultName} and {title[1]} was {fuzz.partial_ratio(resultName, title[1])} and the score for artist similarity between {resultArtists} and {title[0]} was {fuzz.partial_ratio(resultArtists, title[0])}")
#                     missed.append(title)
#         else:
#             print(f"{title[1]} {title[0]} could not be found")


                
        

#     #print(len(song_titles_toSearch))
# # print(f"there were {len(song_titles_toSearch)} songs in the original list, and {len(anotherlist)} songs in the found ones, so {len(song_titles_toSearch) - len(anotherlist)} songs were missed")
#     sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=anotherlist)
#     print(len(anotherlist))


# addSongs()
# addSongs()

#i should use the aforementioned method to add the ids of all the songs in the playlist to a like text file or some permantent storage, and befoer adding the song ot the plauylsit, ti check whether or not the song is in the list of ids already in teh playlsit, and if not, only hten it appensds
# i already have a list of all the ids in the playlist so each time i run the program i'll check if the id is in the file, and if no ti append it to the list of stuff to add to the playlist. after the stuff is appended, then i write the list to the list of ids in the playlist
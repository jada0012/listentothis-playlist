import os 
import pathlib
import praw
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz
import schedule
import time
from dotenv import load_dotenv
from requests.exceptions import ReadTimeout
load_dotenv()

ID_PATH = pathlib.Path.cwd() / "ids.txt"

SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"

sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE), requests_timeout=10, retries=10)
#sp.user_playlist_create(user='5kbehkqoyiok15qrj7uxo55d4', name='Listen to This 2.0', public=True, collaborative=False, description="testing out spotipy")

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
    

playlists = sp.current_user_playlists()
# for i in playlists['items']:
#     if i['name'] == "Listen to This 2.0":
#         PLAYLIST_ID =  i['id']
PLAYLIST_ID = "08TPAp9HipWlCL60vu54Hl"

with open(ID_PATH) as f:
    inplaylist = [line.rstrip() for line in f]



# for track in get_playlist_tracks(PLAYLIST_ID):
#     trackid  = track['track']['id']
#     inplaylist.append(trackid)

# with open('ids.txt', 'a') as f:
#     for track in inplaylist:
#         f.write(track)
#         f.write('\n')

reddit = praw.Reddit(
    client_id = os.getenv('REDDIT_CLIENT_ID'),
    client_secret = os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent = os.getenv('USER_AGENT'),
)
def addSongs(time):
    subreddit = reddit.subreddit("listentothis")
    
    song_titles_toSearch = []
    similarity = 71
    anotherlist = []
    missed = []

    for submission in subreddit.top(time):
        if "[" in submission.title:
            x = submission.title.index('[')
        song = submission.title[:x].lower()
        if song :
            song_titles_toSearch.append(song)
        
    for title in song_titles_toSearch:

        if "--" in title:
            title = title.split('--')
        elif "- -" in title:
            title = title.split('- -')
        
        elif '—' in title:
            title = title.split('—')
        elif '–' in title:
            title = title.split('–')
        elif '-' in title:
            title = title.split('-')
        try:

            results = sp.search(q="track:" + title[1] + title[0], type="track")
        except ReadTimeout:
            print("timeout so time to try again!")
            results = sp.search(q="track:" + title[1] + title[0], type="track")



        if len(results['tracks']['items']) != 0:
            for result in results['tracks']['items']:
                resultName  = result['name'].lower()
                resultArtists =  result['artists'][0]['name'].lower()
                titleArtist = resultName + '--' + resultArtists

                if (fuzz.partial_ratio(resultName, title[1]) >= similarity) and (fuzz.partial_ratio(resultArtists, title[0])) >= similarity:
                    if not result['id'] in anotherlist and not result['id'] in inplaylist:
                        anotherlist.append(result['id'])
                    
                        break



    sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=anotherlist)
    with open(ID_PATH, 'a') as f:
        for line in anotherlist:
            f.write(line)
            f.write('\n')
                
    
    
    
# print(ID_PATH)
choice = int(input("have you missed one day or many? (1 and 2 respectively)"))
if choice == 1:
    addSongs("day")
if choice == 2:
    addSongs("week")
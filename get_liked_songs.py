import spotipy
import os
import json
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get('CLIENT_ID_SRC')
client_secret = os.environ.get('CLIENT_SECRET_SRC')
redirect_uri = os.environ.get('REDIRECT_URI')

scope = 'user-library-read'

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

current_user = sp.current_user()
print(f"Utilisateur connecté : {current_user['display_name']}")

#get the songs
NB_LIKED_SONGS = 1000
response = {}
i=0
while i<NB_LIKED_SONGS:
    results = sp.current_user_saved_tracks(offset=i, limit=50)
    response[i] = results
    i+=50

#dump to json
with open('spotify_data.json', 'w') as fp:
    json.dump(response, fp)

os.remove(".cache")

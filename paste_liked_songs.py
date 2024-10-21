import spotipy
import os
import json
from spotipy.oauth2 import SpotifyOAuth

SONGS_FILE = "spotify_data.json"

client_id = os.environ.get('CLIENT_ID_DEST')
client_secret = os.environ.get('CLIENT_SECRET_DEST')
redirect_uri = os.environ.get('REDIRECT_URI')


scope = 'user-library-modify'

# Authentification OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

uris = []

with open(SONGS_FILE, 'r') as fp:
    response = json.load(fp)

for results in response.values():
    for item in results['items']:
        track = item['track']
        uris.append(track['uri'])

i = 0
increment = 99
while i < len(uris)+increment:
    try:
        sp.current_user_saved_tracks_add(uris[i: i+increment])
    except spotipy.exceptions.SpotifyException:
        pass
    i += increment

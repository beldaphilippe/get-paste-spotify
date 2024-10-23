""" make the specified Spotify account
like the songs and follow the artists
that are in SONGS_FILE """

import spotipy
import os
import json
from spotipy.oauth2 import SpotifyOAuth


SONGS_FILE = "spotify_data.json"

def spotify_authenticate():
    """ Spotify authentication with spotipy """
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
    return sp


def paste_liked_songs(uris):
    i = 0
    increment = 30
    while i+increment <= len(uris):
        try:
            response = sp.current_user_saved_tracks_add(uris[i: i+increment])
            if response != None:
                print(f"Réponse de l'API : {response}")
        except spotipy.exceptions.SpotifyException:
            pass
        i += increment


def follow_artists(ids):
    i = 0
    increment = 30
    while i+increment <= len(ids):
        try:
            response = sp.user_follow_artist(ids[i: i+increment])
            if response != None:
                print(f"Réponse de l'API : {response}")
        except spotipy.exceptions.SpotifyException:
            pass
        i += increment


def main():
    spotify_authenticate()
    with open(SONGS_FILE, 'r') as fp:
        response = json.load(fp)
    songs = response['liked_songs']
    artists = response['followed_artists']
    
    paste_liked_songs(songs)
    follow_artists(artists)

    os.remove(".cache")

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
    client_id = os.environ.get('CLIENT_ID_DEST')
    client_secret = os.environ.get('CLIENT_SECRET_DEST')
    redirect_uri = os.environ.get('REDIRECT_URI')

    scope = 'user-library-modify, user-follow-modify'

    # Authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope,
                                                   cache_path=None))

    current_user = sp.current_user()
    print(f"Utilisateur connecté : {current_user['display_name']}")
    return sp


def paste_liked_songs(sp, uris):
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


def follow_artists(sp, ids):
    i = 0
    increment = 30
    while i+increment <= len(ids):
        try:
            response = sp.user_follow_artists(ids[i: i+increment])
            if response != None:
                print(f"Réponse de l'API : {response}")
        except spotipy.exceptions.SpotifyException:
            pass
        i += increment


def main():
    sp = spotify_authenticate()
    with open(SONGS_FILE, 'r') as fp:
        response = json.load(fp)
    songs = response['liked_songs']
    artists = response['followed_artists']

    paste_liked_songs(sp, songs)
    follow_artists(sp, artists)

    os.remove(".cache")


main()

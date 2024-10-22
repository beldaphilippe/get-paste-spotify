""" put user's liked songs and followed artists"""

import spotipy
import os
import json
from spotipy.oauth2 import SpotifyOAuth


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


def get_liked_songs():
    """ Get the liked songs """
    MAX_LIKED_SONGS = 8000
    response = []
    i=0
    while i<MAX_LIKED_SONGS:
        results = sp.current_user_saved_tracks(offset=i, limit=50)
        if results == []:
            break
        response += results
        i += 50
    return response


def get_followed_artists():
    """ Get the followed artists """
    MAX_FOLLOWED_ARTISTS = 8000
    response = []
    i=0
    while i<MAX_FOLLOWED_ARTISTS:
        results = sp.current_user_followed_artists(offset=i, limit=20)
        if results == []:
            break
        response += results
        i += 20
    return response


def main():
    spotify_authenticate()
    data = {}
    data["liked_songs"] = get_liked_songs()
    data["followed_artists"] = get_followed_artists()

    # Dump to json
    with open('spotify_data.json', 'w') as fp:
        json.dump(data, fp)

    os.remove(".cache")


main()

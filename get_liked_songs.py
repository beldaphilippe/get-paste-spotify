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
    """ Returns the list of uris the liked songs """
    results_uris = []
    i = 0
    results = sp.current_user_saved_tracks(offset=i)
    while results != []:
        for item in results['items']:
            results_uris.append(item['track']['uri'])
        i += 50
        results = sp.current_user_saved_tracks(offset=i)
    return results_uris


def get_followed_artists():
    """ Get the followed artists """
    artists_ids = []
    i = 0
    results = sp.current_user_followed_artists(offset=i)
    while results != []:
        for item in results['item']:
            artists_ids.append(item['artist']['id'])
        i += 20
        results = sp.current_user_followed_artists(offset=i)
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

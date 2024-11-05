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

    scope = 'user-library-read, user-follow-read'

    # Authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope,
                                                   cache_path=None))

    current_user = sp.current_user()
    print(f"Utilisateur connecté : {current_user['display_name']}")
    return sp


def get_liked_songs(sp):
    """ Returns the list of uris the liked songs """
    results_uris = []
    i = 0
    results = sp.current_user_saved_tracks(offset=i)
    while results['items'] != []:
        for item in results['items']:
            results_uris.append(item['track']['uri'])
        i += 50
        results = sp.current_user_saved_tracks(offset=i)
    return results_uris


# def get_followed_artists(sp):
    # """ Get the followed artists """
    # after = None
    # artists_ids = []
    # results = sp.current_user_followed_artists(after=after)
    # while results['artists']['items'] != []:
        # print('a')
        # for item in results["artists"]["items"]:
            # artists_ids.append(item['id'])
        # after = results['artists']['cursors']['after']
        # results = sp.current_user_followed_artists(after=after)
    # return response


def get_followed_artists(sp):
    """ Get the followed artists """
    limit = 20
    after = None
    artists_ids = []
    while True:
        response = sp.current_user_followed_artists(limit=limit, after=after)
        for item in response["artists"]["items"]:
            artists_ids.append(item['id'])
        if not response['artists']['cursors']['after']:
            break
        after = response['artists']['cursors']['after']
    return artists_ids

def main():
    sp = spotify_authenticate()
    data = {}
    data["liked_songs"] = get_liked_songs(sp)
    data["followed_artists"] = get_followed_artists(sp)

    # Dump to json
    with open('spotify_data.json', 'w') as fp:
        json.dump(data, fp)

    # os.remove(".cache")


main()

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
playlist_from_id = os.getenv('PLAYLIST_FROM_ID')
playlist_to_id = os.getenv('PLAYLIST_TO_ID')

if client_id is None or len(client_id) == 0:
    print("Missing SPOTIPY_CLIENT_ID environment variable")
    exit(1)

if client_secret is None or len(client_secret) == 0:
    print("Missing SPOTIPY_CLIENT_SECRET environment variable")
    exit(1)

if playlist_from_id is None or len(playlist_from_id) == 0:
    print("Missing PLAYLIST_FROM_ID environment variable")
    exit(1)

if playlist_to_id is None or len(playlist_to_id) == 0:
    print("Missing PLAYLIST_TO_ID environment variable")
    exit(1)

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

from_playlist_items = spotify.playlist_items(playlist_from_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))

uris = [item["track"]["uri"] for item in from_playlist_items["items"]]

# items - a list of track/episode URIs or URLs
# Does not work with client credentials unfortunately.....
spotify.playlist_add_items(playlist_to_id, uris, position=None)

print("Succesfully archived " + len(uri) + " items")
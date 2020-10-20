# set SPOTIPY_CLIENT_ID='66788a5caa9c4e408c92827077e4e7e2'
# set SPOTIPY_CLIENT_SECRET='e996f4ccde12449baa146590b823bac4'
# set SPOTIPY_REDIRECT_URI='https://nathan-logan.github.io/spotify-overlay/callback'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
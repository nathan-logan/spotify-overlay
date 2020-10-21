import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk


def currently_playing():
    track_info = sp.current_user_playing_track()
    if not track_info is None:
        return track_info
    return "No track playing"


scope = "user-read-recently-played user-read-playback-position user-top-read playlist-modify-private playlist-read-collaborative playlist-read-private playlist-modify-public streaming user-read-private user-library-read user-read-currently-playing user-read-playback-state user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

res = currently_playing()


window = tk.Tk()

current_song = tk.Label(text='Now playing: ' + res['item']['name'])

current_song.pack()

window.mainloop()

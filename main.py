import os

from spotipy import client
from spotipy.oauth2 import SpotifyClientCredentials
from spotifyClient import *

def run():
    
    # initialize the spotify client 

    username = 'ezsslxv5ofwujfritffl7wu0p'
    sp = spotifyClient(username)
    
    audio = sp.get_audio_file()
    artist = sp.get_artist()
    songName = sp.get_song_name()
    coverArt = sp.get_album_cover_art()

    for i in range(len(audio)):
        print(i, artist[i], songName[i])
        print(audio[i])
        print(coverArt[i])

if __name__ == '__main__':
    run()
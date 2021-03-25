import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

class spotifyClient(object):
    def __init__(self, username):
        scope = 'user-top-read'
        self.token = token = SpotifyOAuth(scope=scope, username=username)
        self.sp = spotipy.Spotify(auth_manager=token)

    def get_top_tracks(self, term = 'short_term'):
        
        # short term - 4 weeks, medium term - 6 months, long term - lifetime
        results = self.sp.current_user_top_tracks(time_range=term, limit=2)
        
        return results

    def get_artist(self):
        
        results = self.get_top_tracks()
        artist = []
        for item in results['items']:
            artist.append(item['artists'][0]['name'])
        
        return artist
    
    def get_song_name(self):
        
        results = self.get_top_tracks()
        songName = []
        for item in results['items']:
            songName.append(item['name'])
        
        return songName
         
    def get_album_cover_art(self):
        
        results = self.get_top_tracks()
        coverArt = []
        for item in results['items']:
            coverArt.append(item['album']['images'][0]['url'])
        # print(coverArt)
        return coverArt

    def get_audio_file(self):

        results = self.get_top_tracks()
        audioFiles = []
        for item in results['items']:
            audioFiles.append(item['preview_url'])
        
        return audioFiles

    # get popularity 

    # get album name
    
    
    
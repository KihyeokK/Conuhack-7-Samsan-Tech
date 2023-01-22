import time
from django.db import models
import text2emotion as te
import json
import spotipy
import webbrowser
# custom user ONLY email
'''
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
'''

fpath = ""

# Create your models here. 
class Diary(models.Model):
    author = models.ForeignKey('auth.User', related_name='diaries', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default="no title", unique=True)
    content = models.TextField(default="Write Here")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_liked = models.BooleanField(default=False)
    mood = models.CharField(max_length=10, null=True, blank=True)
    music = models.URLField(max_length=200, null=True, blank=True)
    def extract_mood(self, *args, **kwargs):
        """()->str
        emotions: 'Angry', 'Fear', 'Happy', 'Sad', 'Surprise'
        if every emotion has the same numerical scale, then...
        """
        d_emotions = te.get_emotion(self.content)
        emotion_max = max(d_emotions, key=d_emotions.get)
        emotion_min = min(d_emotions, key=d_emotions.get)
        if emotion_max == emotion_min:
            return "No feeling"
        return emotion_max
    
    def save(self, *args, **kwargs):
        # to update the mood field when we create the object
        if self.content == "Write Here":
            # access the file using the file path
            
            pass
        self.mood = self.extract_mood(self.content)
        self.music = self.play_music()
        super().save(*args, **kwargs)

    def play_music(self, *args, **kwargs):
        username = '31b7rcws54ucl3wqtj2hpn5r5uey'
        clientID = 'ebda86342f1f4cdd94ae46612d5318c5'
        clientSecret = 'b78009b89249482a8b357384d6bab429'
        redirect_uri = 'http://google.com/callback/'
        oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
        # get the token as proof of our authorized access to Spotify.
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']
        # the token generated in the previous step gets authorized.
        spotifyObject = spotipy.Spotify(auth=token)
        user_name = spotifyObject.current_user()
        # This user information is used to retrieve the JSON response sent by the browser to our system. 
        # The print statement here is used to print this JSON response in readable format.
        print(json.dumps(user_name, sort_keys=True, indent=4))
        search_song = self.mood
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        return song
    def _str_(self):
        return self.title
    class Meta:
        ordering = ['created_at']

"""
class Playlist(models.Model):
    # get playlist name and set title to be that name.
    title = models.CharField(max_length=120, default="no title", unique=True)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    # do we need more attributes?
    def _str_(self):
        return self.title
"""
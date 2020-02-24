import spotipy
import spotipy.util as util
import tweepy
import pyperclip
import os
import json
import time
import random
scopes = 'user-library-read playlist-modify-private playlist-modify-public user-library-modify streaming user-read-playback-state'
spotify_client_id = '44743ab488e74b718e7e314601de135e'
spotify_secret = '6375842d113d4679a84196ae54b85034'
spotify_redirect_url = 'https://www.google.com/'
username1 = "zanealgogh"
token = util.prompt_for_user_token(username=username1,scope=scopes,client_id=spotify_client_id,client_secret=spotify_secret,redirect_uri=spotify_redirect_url)
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
print('Spotify User ' + username1 + ' successfully authenticated')
#authenticate twitter user
twitter_consumer = 'OuMcb2WRlqqJwcaGExVWzGGTL'
twitter_consumer_secret = 'nU2VyQqKg3TZokl3uhJprerhiKBnzux3azPUU2eGaI3N4ArzdB'
twitter_access = '1230147815877337088-XuFuvqM7RSbA0gV20EAdxIIMGqKnqS'
twitter_access_secret = '9RgSlaausGllPlq6wBG2b7JkGzzy0Tyd8j5n8Cw2ejUt7'
auth = tweepy.OAuthHandler(twitter_consumer, twitter_consumer_secret)
auth.set_access_token(twitter_access, twitter_access_secret)
api = tweepy.API(auth)
def CurrentSongPlaying():
    songplaying = spotifyObject.currently_playing()
    currentArtist = songplaying['item']['album']['artists'][0]['name']
    currentAlbum = songplaying['item']['album']['name']
    currentTitle = songplaying['item']['name']
    currentURL = songplaying['item']['external_urls']['spotify']
    actuallyPlaying = songplaying['is_playing']
    print('Marcelo is currently playing "' + currentTitle + '" by artist ' + currentArtist + ' ' + currentURL)
    print(actuallyPlaying)
    CurrentTitleMem = currentTitle
    api.update_status('Marcelo is currently playing "' + currentTitle + '" by artist ' + currentArtist + ' ' + currentURL + ' #' + str(random.randint(1, 10000)))


MemSong = ['']
while True:
    songplaying2 = spotifyObject.currently_playing()
    currentTitle2 = songplaying2['item']['name']
    if MemSong[-1] == currentTitle2:
        print('The Same')
    if MemSong[-1] != currentTitle2:
        MemSong.append(currentTitle2)
        print('not')
        CurrentSongPlaying()
    time.sleep(10)
    


import spotipy
import spotipy.util as util
import tweepy
import pyperclip
import os
import json
username1 = "zanealgogh"
scope1 = 'user-library-read playlist-modify-private playlist-modify-public user-library-modify streaming user-read-playback-state'
token = util.prompt_for_user_token(username=username1,scope=scope1,client_id='44743ab488e74b718e7e314601de135e',client_secret='6375842d113d4679a84196ae54b85034',redirect_uri='https://www.google.com/')
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
print('Spotify User ' + username1 + ' successfully authenticated')
def CurrentSongPlaying():
    songplaying = spotifyObject.currently_playing()
    #print(json.dumps(songplaying, sort_keys=True, indent=4))
    pyperclip.copy(json.dumps(songplaying, sort_keys=True, indent=8))
    currentArtist = songplaying['item']['album']['artists'][0]['name']
    currentAlbum = songplaying['item']['album']['name']
    currentTitle = songplaying['item']['name']
    currentURL = songplaying['item']['external_urls']['spotify']
    actuallyPlaying = songplaying['is_playing']
    print('Marcelo is currently playing "' + currentTitle + '" by artist ' + currentArtist + ' ' + currentURL)
    print(actuallyPlaying)

CurrentSongPlaying()
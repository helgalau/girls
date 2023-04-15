## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

import pandas as pd 
import spotipy
from spotipy.oauth2 import SpotifyOAuth

songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")
## print(songs["artist"])
## df2 = songs[["artist","text"]]
artist_list = list(set(songs["artist"])) #no duplicates 
song_list = list(songs["song"]) #songs are unique
link_list = list(songs["link"]) #links are unique to the song, not sure if we want to use, but just in case
lyrics_list = list(songs["text"]) ##includes \r and \n in the list, sep = ,
artist_lyrics = songs[["artist","text"]] #can use to sort by artist and lyrics
artist_title = songs[["artist","song"]] #can use to sort by artist and song, no lyrics
artist_title_lyrics = songs[["artist","song","text"]] #can use to sort by all filterable columns
title_lyrics = songs[["song","text"]] #can use to sort by song name and lyrics

class song_features:
    client_id = "04fe36c0ba5846f4856fc7796ff4eab8"
    client_secret = "9c45909506b247088e7d296bfae4ae54"
    redirect_uri = "http://localhost:9000"
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=client_id,
                                              client_secret=client_secret,
                                              redirect_uri=redirect_uri))
    
    
    
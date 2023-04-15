## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

import pandas as pd # Michelle

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

def listcomp_match():
    
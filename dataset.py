## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 

import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer


song_info = pd.read_csv("Spotify_Youtube.csv")
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

def search_song_lyrics():
    # Get input from user for song lyrics
    search = input("What lyrics do you want to search for?: ")
    
    with open('spotify_millsongdata.csv', 'r', encoding = "utf-8") as f:
        lines = f.readlines()

        # Use a list comprehension to pull the lines that have the search the user wants
        match = [line for line in lines if search in line]
        
        if match:
            print("Matching songs:")
            for line in match:
                print(line)
                
search_song_lyrics()


#clean function using regular expression
def clean_lyrics(text):
  regex = r'[^a-zA-Z\d\s]' #this regex discludes all non-word characters
  return re.sub(regex, "", str(text))

#clean dataframe lyrics
df['cleaned_lyrics'] = df['text'].apply(clean_lyrics)

#use TfidfVectorizer to measure how often words begin to appear in document
#convert TfidfVectorizer into a matrix through NPL vectorization technique 
vectorizer = TfidfVectorizer()
lyric_matrix = vectorizer.fit_transform(df['cleaned_lyrics'])

#take in user's input
user_input = "She's just the girl"  #user_input = input("Give me a lyric: ")
users_cleaned_input = clean_lyrics(user_input)

#take user's cleaned lyrical input and convert to a matrix to compare and find the closest related song
user_matrix = vectorizer.transform(df['cleaned_lyrics'])


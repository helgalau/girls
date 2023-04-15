## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

import pandas as pd 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
    """Connect to Spotify Web API to find details about matched song.
    """
    client_id = "04fe36c0ba5846f4856fc7796ff4eab8"
    client_secret = "9c45909506b247088e7d296bfae4ae54"
    redirect_uri = "http://localhost:9000"
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=client_id,
                                              client_secret=client_secret,
                                              redirect_uri=redirect_uri))
    
    # Connect matched song to spotify API
    # Find song features
    # Print out song info and details
    # Maybe recommend other songs with similar BPM?
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

#load the csv file into pandas df
df = pd.read_csv('spotify_millsongdata.csv')

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

#use cosine similarily in NPL to assess whether the user's lyrics and the song's lyrics are the same
lyrical_similarities = cosine_similarity(lyric_matrix, user_matrix)

#create a sorted list of ranked songs based on their cosine similarites 
ranked_songs = pd.DataFrame({'song': df['song'], 'artist': df['artist'], 'similarity': lyrical_similarities.flatten()})
ranked_songs_sorted = ranked_songs.sort_values('similarity', ascending=False)

#print the top 5 song matches with their similarity scores in comparison's to the user's lyrical input 
top_5_songs = ranked_songs_sorted[['song', 'artist', 'similarity']].head(5) #use the .head() function to get the top 5 song matches
print(top_5_songs)

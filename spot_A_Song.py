## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 

import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer

song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")

#pandas stuff
#merge + drop columns turn each column into a list

class Song:
    def __init__(self):
        pass
    def regexGroup(self):
        regex = r"""\w""" # not actually done
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
def main():
    search_song_lyrics()            
        
    if __name__ == "__main__":
        main()

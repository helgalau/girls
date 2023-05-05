## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 
import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer 

def pandas():
    song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
    songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")
    songs = songs.drop("link", axis = 1)
    song_info = song_info.drop(["Danceability","Energy", "Key",
                            "Loudness","Speechiness","Acousticness",
                            "Instrumentalness","Liveness", "Valence", "Tempo", "Title", "Channel", "Likes", 
                            "Comments","Description","Licensed","official_video","Unnamed: 0"], axis = 1)

    df = songs.merge(song_info, left_on = ["artist","song"], right_on= ["Artist","Track"])
    df = df.drop("Artist", axis = 1)
    df = df.drop("Track", axis = 1)
    x =df.to_numpy().tolist()
    #x= df[df["artist"] == "ABBA"].values.tolist()
    ## if they know the artist, we can search from here or use regex/list comp

    with open('filename2.txt', 'w') as f:
        for items in x:
            f.write("%s\n" % items)

    with open('filename2.txt', 'r') as g:
        for y in g:
            print(y)
            
def regexGroup():
        with open('filename2.csv', 'r', encoding = "utf-8") as f:
            lines = f.readlines()
        regex = r""""(?x)
                    ^\['(?P<artist>.+?)',
                    \s'(?P<name> .+?)',
                    \s\"(?P<lyrics> .+?)\",
                    \s'(?P<spotifyLink> .+?)',
                    \s'(?P<albumName> .+?)',
                    \s'(?P<albumType> .+?)',
                    \s'(?P<track> .+?)',
                    \s(?P<duration> .+?),
                    \s(?P<youtube>.+?)',
                    \s(?P<views>.+?),
                    \s(?P<streams>.+?)]
                """
        match = re.search(regex, lines)
        return match
        
class Song:
    def __init__(self):
        self.arists = []
        self.lyrics = []
        self.links = []
        self.duration = []
      
    def search_song_lyrics(self, lyrics_search, artist_search):
        regex_call = regexGroup()
        # Use a list comprehension to pull the lines that have the search the user wants
        lyrics_match = [match for match in regex_call if artist_search in match]
        if lyrics_match:
            return lyrics_match
                    
        artist_match = [match.group('artist') for match in regexGroup()]
        if artist_match:
            return artist_match 
            
    def artist_and_song():
        pass
    
    
def main():
    # Get input from user for song lyrics and artist name
     lyrics_search = input("What lyrics do you want to search for?: ")
     artist_search = input("What is the name of the artist?: ")
     x = Song()
     x.search_song_lyrics(lyrics_search, artist_search)
     # Displays the matching songs and artists
     print(f"The possible matching song(s) are: {x.lyrics_match}")          
     print(f" The possible artist(s) are: {x.artist_match}")   
     
if __name__ == "__main__":
     main()

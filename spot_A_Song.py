## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 
import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer 

def pandas():
    song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
    songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")
    songs = songs.drop("link", axis = 1)
    song_info = song_info.drop("Danceability", axis = 1)
    song_info = song_info.drop("Energy", axis = 1)
    song_info = song_info.drop("Key", axis = 1)
    song_info = song_info.drop("Loudness", axis = 1)
    song_info = song_info.drop("Speechiness", axis = 1)
    song_info = song_info.drop("Acousticness", axis = 1)
    song_info = song_info.drop("Instrumentalness", axis = 1)
    song_info = song_info.drop("Liveness", axis = 1)
    song_info = song_info.drop("Valence", axis = 1)
    song_info = song_info.drop("Tempo", axis = 1)
    song_info = song_info.drop("Title", axis = 1)
    song_info = song_info.drop("Channel", axis = 1)
    song_info = song_info.drop("Likes", axis = 1)
    song_info = song_info.drop("Comments", axis = 1)
    song_info = song_info.drop("Description", axis = 1)
    song_info = song_info.drop("Licensed", axis = 1)
    song_info = song_info.drop("official_video", axis = 1)
    song_info = song_info.drop("Unnamed: 0", axis = 1)

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
        
class Song:
    def __init__(self):
        pass
    
    def regexGroup(self):
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
    x = Song()
    x.search_song_lyrics()            
        
    if __name__ == "__main__":
        main()

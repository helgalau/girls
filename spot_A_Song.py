"""Script that allows the user to type in lyrics, artist (if applicable)
to search for their desired song or list of similar songs. Additionally, it 
provides the song's duration time, spotify link, youtube link, and danceability
score.

## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 
"""

import matplotlib.pyplot as plt
import pandas as pd 
import re
"""A module for finding a song match based on lyrics and artist."""

def mergefiles():
    """Opens up the two csv files containing the songs' information and 
    combines them. Then the combined data is turned into a list that is stored
    in a txt file.
    
    Returns:
        df(Pandas Dataframe): New dataframe that includes the songs information
    
    Side effects:
        Creates filename2.txt and populates it with a dataframe information;
        Merges 2 different csv files and drop selected columns
    """
    song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
    songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")
    songs = songs.drop("link", axis = 1)
    song_info = song_info.drop(["Energy", "Key",
                            "Loudness","Speechiness","Acousticness",
                            "Instrumentalness","Liveness", "Valence", "Tempo",
                            "Title", "Channel", "Likes", "Comments",
                            "Description","Licensed","official_video",
                            "Unnamed: 0"], axis = 1)

    df = songs.merge(song_info, left_on = ["artist","song"],
                     right_on= ["Artist","Track"])
    df = df.drop("Artist", axis = 1)
    df = df.drop("Track", axis = 1)
    x =df.to_numpy().tolist()
    
    with open('filename2.txt', 'w') as f:
            for items in x:
                f.write("%s\n" % items)
                
    return df
            
def regexGroup():
    """Groups the information from the file that contains the song information.
    
    Returns:
        match(list of str): an iterator yielding match objects from the matching
            group
    """
    with open('filename2.txt', 'r', encoding = "ANSI") as f:
        lines = f.readlines()
        text = ''.join(lines)
    regex = r"""(?xm)^\['(?P<artist>.+?)',
                \s'(?P<name>.+?)',
                \s\"(?P<lyrics>.+?)\",
                \s'(?P<spotifyLink>.+?)',
                \s'(?P<albumName>.+?)',
                \s'(?P<albumType>.+?)',
                \s'(?P<track>.+?)',
                \s(?P<duration>.+?),
                \s(?P<youtube>.+?)',
                \s(?P<views>.+?),
                \s(?P<streams>.+?)\]
            """
    match = re.finditer(regex, text)
    return match
        
class Song:
    """This class keeps track of all songs being inputted
    by the user and processed.
    
    Attributes:
        artists(list of str): artist names
        lyrics(list of str): Lyrics in the song
        links(list of str): links associated with the song
        duration(list of str): how long the song is
    """
    def __init__(self):
        """Initializes the artists, lyrheics, links, and durations
           of the songs in an empty list.
        """
        self.artists = []
        self.lyrics = []
        self.links = []
        self.duration = []
        self.datafr = mergefiles()
      
    def search_song_lyrics(self, lyrics_search, artist_search = "not given"):
        """ Finds a match for the lyrics and the artist that
            the user inputed.
            
        Args:
            lyrics_search (list of strings): lyrics that the user inputed
            artist_search (list of strings): artist that the user inputed
            
        Returns:
            lyrics_match: the matching lyrics
            artist_match: the matching artist  
        """
        reg_match = regexGroup()
       
        #for match in regex_matches

        if artist_search == "not given":
             lyrics_match = [match.group('name') for match in reg_match if
                            lyrics_search in match.group('lyrics')]
        else:
            lyrics_match = [match.group('name') for match in reg_match if
                            lyrics_search in match.group('lyrics') and
                            artist_search in match.group('artist')]
            
        self.lyrics.append(lyrics_match)
        self.artists.append(artist_search)      

        return (lyrics_match[0], artist_search)
    
    
    def check_availability(lyrics_search, artist_search = "not given"):
        """Checks the validity of the user's lyrical or artist input. 
        If the user has inputted an invalid lyric or artist name, it alerts the
        user through an informal string representation that it is invalid.
        
        Args:
            lyrics_search (list of strings): user's inputted lyrics
            artist_search (list of strings): user's inputted artist, default
            key is "not given"
            
        Returns:
            Boolean value from conditional expression based off of the user's 
            lyrical input or artist input. 
        """
        reg_match = regexGroup()
        # for song in x:
        if artist_search == "not given":
            match = [match.group('lyrics') for match in reg_match if
                            lyrics_search in match.group('lyrics')]
        else: 
            match = [match.group('artist') for match in reg_match if
                            artist_search in match.group('artist')]
        
        #Conditional Expression
        return False if match == [] else True
            

    
    def data_vis(self, song):
        """Creates two data visualization bar graphs based on users' song 
        input. Bar graph 1 displays the user's bar graph to its corresponding
        danceability score. Bar graph 2 displays the top 5 songs with the 
        highest danceability score to allow user's to compare the users' song
        danceability score to the top 5 songs. 
        
        Args:
            song (str): user's inputted song
        
        Returns:
        Two data visualization graphs: 
            1. User's Song vs Danceability Score
            2. Top 5 Songs with the highest danceability scores
        """
        #Data Visualization: Bar Graph for user's inputted song and
        #danceability score
        df = self.datafr
        
        df_song = df[df["song"] == song]
        
        plt.bar(df_song['song'], df_song['Danceability'])
        
        plt.xlabel("Song")
        plt.ylabel("Danceability")
        plt.title(f"Danceability for {song}")
        plot_results = plt.show()
        
        #Data Visualization #2: Sort the danceability score in descending order 
        #to get the top 5 danceability scores
        top_5_dance_scores = df.sort_values('Danceability',
                                            ascending = False).head(5)

        plt.bar(top_5_dance_scores['song'], top_5_dance_scores['Danceability'])
        plt.xticks(rotation=90)
        plt.xlabel("Song")
        plt.ylabel("Danceability Score")
        plt.title("Top 5 Songs by Danceability Score")
        top_5_songs_plot_results = plt.show()
        
    
    def get_duration_and_links(self): 
        """Gets the duration and YouTube and Spotify links from dataframe.
        
        Returns:
            duration (str): length of song in minutes and seconds
            yt_link (str): YouTube link for song
            sp_link (str): Spotify link for song 
        """
        df = mergefiles()
        if self.artists[0] != 'not given':
            filtered = df[(df['song'].isin(self.lyrics[0])) & 
                          (df['artist'] == self.artists[0])]
        else:
            filtered = df[(df['song'].isin(self.lyrics[0]))]
        dur = str(filtered['Duration_ms']).split()[1]
        duration = "%.2f" % (float(dur)/60000)
        yt_link = str(filtered['Url_youtube']).split()[1]
        sp_link = str(filtered['Url_spotify']).split()[1]
        
        return duration, yt_link, sp_link
        
            
    def __str__(self):
        """Return link and duration for the top match.
        
        Returns:
            (str): Song details with name, links, and length
        """
        duration, youtube, spotify = self.get_duration_and_links()

        return f""" Song: {self.lyrics[0]} by {self.artists[0]}
                    Youtube Link: {youtube}
                    Spotify Link: {spotify}
                    Song length: {duration[0]} minutes and {duration[2:]} seconds"""
    
def main():
    """
    This function will take input (lyrics and artist) from the user, 
    process that input, and produces a match to their desired inputs. 
    """
    # Get input from user for song lyrics and artist name
    print("Welcome to Spot-A-Song!")
    availabilityCheck = False
    artistCheck = False
    
    lyrics_search = input("What lyrics do you want to search for?: ")
    
    #Iterates until user inputs a valid input (lyric and artist) for the 
    #check_availability method
    while(availabilityCheck is False):
        if (Song.check_availability(lyrics_search) is True):
            artist_search = input("What is the name of the artist? (Put \"not given\" if unknown ): ")
            while(Song.check_availability(lyrics_search, artist_search) is False):
                print("Invalid artist")
                artist_search = input("What is the name of the artist? (Put \"not given\" if unknown ): ")
            availabilityCheck = True
        else:
            print("Invalid lyrics")
            lyrics_search = input("What lyrics do you want to search for?: ")
            
    x = Song()
     
    results = x.search_song_lyrics(lyrics_search, artist_search)
    results2 = ', '.join(results)
    
    # Displays the matching songs and artists
    print(f"The possible matching song(s) are: {x}")  
    
    #Gets the input from user for song name to calculate and produce data viz        
    danceability_search = input("Can you dance to this song? Input your song name! ")
    x.data_vis(danceability_search)
     
     
if __name__ == "__main__":
     main()

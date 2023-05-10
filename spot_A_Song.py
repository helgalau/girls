"""I think we need a docstring for the project?"""
"""Use filename2.txt for seraching song lyrics"""
## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 

import matplotlib.pyplot as plt
import pandas as pd 
import re
#from sklearn.feature_extraction.text import TfidfVectorizer 

def mergefiles():
    """Opens up the two csv files containing the songs' information and 
    combines them. Then the combined data is turned into a list that is stored in a txt file.
    
    Side effects:
    Creates filename2 and populates it with 
    """
    song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
    songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")
    songs = songs.drop("link", axis = 1)
    song_info = song_info.drop(["Energy", "Key",
                            "Loudness","Speechiness","Acousticness",
                            "Instrumentalness","Liveness", "Valence", "Tempo",
                            "Title", "Channel", "Likes", "Comments","Description",
                            "Licensed","official_video","Unnamed: 0"], axis = 1)

    df = songs.merge(song_info, left_on = ["artist","song"], right_on= ["Artist","Track"])
    df = df.drop("Artist", axis = 1)
    df = df.drop("Track", axis = 1)
    x =df.to_numpy().tolist()
    #x= df[df["artist"] == "ABBA"].values.tolist()
    ## if they know the artist, we can search from here or use regex/list comp

    with open('filename2.txt', 'w') as f:
        for items in x:
            f.write("%s\n" % items)

    #with open('filename2.txt', 'r') as g:
       # for y in g:
            #print(y)
          #  pass
          
    return df
            
def regexGroup():
    """Groups the information from the file that contains the song information.
    
    Returns:
        match(list of str)    
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
    def __init__(self):
        """Initializes the artists, lyrheics, links, and durations
           of the songs in an empty list.
        """
        self.artists = []
        self.lyrics = []
        self.links = []
        self.duration = []
      
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
                            lyrics_search in match.group('lyrics') and artist_search in match.group('artist')]
            
        self.lyrics.append(lyrics_match)
        self.artists.append(artist_search)
       
        #if artist_search != "not given": 
          # artist_match = [match.group('name') for match in lyrics_match if
            #              artist_search in match.group('artist')]
        
           # return lyrics_match, artist_match
        # Use list comprehension to pull matching lyrics
        #return lyrics_match
        #Use list comprehension to pull matching artists        
 
        return (lyrics_match[0], artist_search)
    
    
    def check_availability(self):
        #Conditional Expression
        
        return ("unavailable") if (lyrics_search not in x) or (artist_search not in x) else "availible"
        
        search_song_lyrics()
        #NO
    
    def data_vis(self, song):
        #Data Visualization: Bar Graph for user's inputted song and danceability score
        df1 = mergefiles()
        
        df_song = df1[df1["song"] == song]
        
        plt.bar(df_song['song'], df_song['danceability'])
        
        plt.xlabel("Song")
        plt.ylabel("Danceability")
        plt.title(f"Danceability for {song}")
        plot_results = plt.show()
        #Data Visualization #2: Sort the danceability score in descending order to get the top 5 danceability scores
        top_5_dance_scores = df1.sort_values('Danceability', ascending = False).head(5)

        plt.bar(top_5_dance_scores['song'], top_5_dance_scores['Danceability'])
        plt.xticks(rotation=90)
        plt.xlabel("Song")
        plt.ylabel("Danceability Score")
        plt.title("Top 5 Songs by Danceability Score")
        top_5_songs_plot_results = plt.show()
        
    
    def unpack(self):
        """ Utilize sequence unpacking to return the lyrics and artist name.
        """
        s = Song()
        lyrics, artist = s.lyrics[0], s.artists[0]
    
        return lyrics, artist
            
    def __str__(self):
        """Return link and duration for the top match.
        
        Returns:
            (str): Song details with name, links, and length
        """
        u = unpack()
        df = pandas()
        if u[1] != 'not given':
            filtered = df[(df['song'] == u[0]) & (df['artist'] == u[1])]
        else:
            filtered = df[(df['song'] == u[0])]

        yt_link = str(filtered['Url_youtube']).split()[1]
        sp_link = str(filtered['Url_spotify']).split()[1]
        dur = str(filtered['Duration_ms']).split()[1]
        duration = "%.2f" % ((dur)/60000)


        return f""" Song: {u[0]} by {u[1]}
                    Youtube Link: {yt_link}
                    Spotify Link: {sp_link}
                    Song length: {duration[0]} minutes and {duration[2:]} seconds"""
    
def main():
    # Get input from user for song lyrics and artist name
     lyrics_search = input("What lyrics do you want to search for?: ")
     artist_search = input("What is the name of the artist? (Put \"not given\" if unknown ): ")
     x = Song()
     #Displayes the second bar graph of the top 5 danceability scores and songs -> gives users ability to compare their song to the top 5 songs to see if it has a high danceability score
     
     
     results = x.search_song_lyrics(lyrics_search, artist_search)
     results2 = ', '.join(results)
    
     # Displays the matching songs and artists
     print(f"The possible matching song(s) are: {x}")          
     danceability_search = input("Want to add this song to your party playslist? Check to see if you can dance to this song! What is your song name? ")
     #Displays the first bar graph of the user's inputted song and danceability score
     x.data_vis(danceability_search)
     
     
if __name__ == "__main__":
     main()

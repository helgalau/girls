"""I think we need a docstring for the project?"""
"""Use filename2.txt for seraching song lyrics"""
## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 
import pandas as pd 
import re
#from sklearn.feature_extraction.text import TfidfVectorizer 

def pandas():
    """Opens up the two csv files containing the songs' information and 
    combines them. Then the combined data is turned into a list that is stored in a txt file.
    
    Side effects:
    Creates filename2 and populates it with 
    """
    song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
    songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")
    songs = songs.drop("link", axis = 1)
    song_info = song_info.drop(["Danceability","Energy", "Key",
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
        """Initializes the artists, lyrics, links, and durations
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
       
        #if artist_search != "not given": 
          # artist_match = [match.group('name') for match in lyrics_match if
            #              artist_search in match.group('artist')]
        
           # return lyrics_match, artist_match
        # Use list comprehension to pull matching lyrics
        #return lyrics_match
        #Use list comprehension to pull matching artists        
         
        return (lyrics_match[0], artist_search)
            
    
def main():
    # Get input from user for song lyrics and artist name
     lyrics_search = input("What lyrics do you want to search for?: ")
     artist_search = input("What is the name of the artist? (Put \"not given\" if unknown ): ")
     x = Song()
     results = x.search_song_lyrics(lyrics_search, artist_search)
     results2 = ', '.join(results)
     # Displays the matching songs and artists
     print(f"The possible matching song(s) are: {results2}")          
     #print(f" The possible artist(s) are: {x.artist_match}")
     
     return results
     
     
def unpack():
    """ Utilize sequence unpacking to return the lyrics and artist name.
    """
    m = main()

    lyrics, artist = m[0], m[1]
  
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


  return f"""Song: {u[0]} by {u[1]}
            Youtube Link: {yt_link}
            Spotify Link: {sp_link}
            Song length: {duration[0]} minutes and {duration[2:]} seconds"""
     
if __name__ == "__main__":
     main()

## link to csv -> https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
## link to csv 2 -> https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube 

import pandas as pd 
import re
from sklearn.feature_extraction.text import TfidfVectorizer

song_info = pd.read_csv("Spotify_Youtube.csv", sep = ",")
songs = pd.read_csv("spotify_millsongdata.csv", sep = ",")

#pandas stuff
#merge + drop columns turn each column into a list

class song:
    def __init__(self):
        pass
    def regexGroup(self):
        regex = r"""\w""" # not actually done
    
    
def main():
    pass

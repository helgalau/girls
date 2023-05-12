## Files:

1. **spot_millsongdata.csv**: Utilized this csv file to access artists, songs, links, and corresponding lyrics
2. **Spotify_Youtube.csv**: Utilized this csv file to access additional set of songs, albums, danceability scores, spotify_url link, youtube_url link, & song duration.
    - These csv files were merged into a dataframe using Pandas to create data visualization bar graphs and access critical columns such as spotify_url links, youtube_url links, song duration, and a songs' danceability score. 
3. **.gitattributes**: Used to add spot_millsongdata.csv and Spotify_Youtube.csv to git
3. **filename2.txt**: This text file was created as a result of converting the merged dataframe of both csv files into a list of strings to allow our regex() function to parse through the strings and group them using regular expressions.
4. **spot_A_Song.py**: This python script was created to develop our game, "Spot-A-Song" which contains our Song class, functions, and methods to allow the user to type in the lyrics they want to search for in the prompt line and the artist (if applicable, but this step is optional) to produce their desired song or list of similar songs. Additionally, it provides the song's duration time, spotify link, youtube link in the console as well as the users' song's danceability score in the form of data visualization bar graph. 

## Instructions to run Spot-A-Song:
1. First, type in **python spot_A_Song** on Windows to **python2 spot_A_Song** on Mac to run our program
2. Next, you will be prompted with the following statments:
   
   **Welcome to Spot-A-Song!**
   
   **What lyrics do you want to search for?:**
   
   Type in **exact** lyrics from our filename2.txt.
   
   _- Note 1: Our program is case-sensitive so please type in the exact uppercase and lowercase lyrics to the program_
   
   _- Note 2: If you type in any lyrics that are not from our text file or numbers into the program, you will be prompted with the "invalid lyrics" until you type in a valid string of lyrics_
3. Once you've inputted your desired lyrics, you will be prompted with the following question:

   **What is the name of the artist? (Put "not given" if unknown ):**
   
   Type in the artist's name. If the artist is unknown, type in "not given".
   
   _- Note 1: Our program is case-sensitive so please type in the exact uppercase and lowercase name of the artist to the program_
   
   _- Note 2: If you type in an artist's name that is not from our text file or numbers into the program, you will be prompted with the "invalid artist" until you type in a valid artist's name_

4. If you typed in a specific artist's name, you will be given the exact matching song and the artist's name. However, if you typed in "not given", you will be given a list of all of the possible matching songs that match the lyrics you inputted into the system as well as the closest artist match. Additionally, you will be providied with the song's metadata:

    **Youtube Link:**
    
    **Spotify Link:**
    
    **Song length:**
    
5. Finally, you will be given the opportunity to type in the song name to determine it's danceability score through two bar graphs. 

   **Can you dance to this song? Input your song name!**
   
   Please exit the first bar graph which is a data visualization of your song and its danceability score to view the top 5 songs with the highest danceability score bar graph. These bar graphs were made so the user can compare their song's danceability score to the top 5 songs with the highest danceability score to see how **hype** and **danceable** their song is!


## Attributes:

| Method/function | Primary author |  Techniques demonstrated |
| -------------   | -------------  | -------------------------|
| mergefiles()      | Emily Wright  | pandas merge & drop |
| regexGroup()      | Emily Wright   | regular expressions |
| get_duration_and_links()    | Michelle Nguyen   | filtering w/ Pandas (not claiming) |
| __str__()    | Michelle Nguyen   | magic methods, sequence unpacking |
| search_song_lyrics    | Helga Lau   | list comprehension |
| main()    | Helga Lau   | f-strings |
| check_availability()    | Roshini Saravanan   | conditional expressions |
| data_vis()   | Roshini Saravanan   | visualizing data w/ pyplot & Pandas dataframe (not claiming) |

## Sources:

Mahajan, Shrirang. (2022, December 11). "Spotify Million Song Dataset." 
https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

Rastelli, Salvatore. (2023, March 11). "Spotify and Youtube." 
https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube

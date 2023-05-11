## Files:

1. **spot_millsongdata.csv**: Utilized this csv file to access artists, songs, links, and corresponding lyrics
2. **Spotify_Youtube.csv**: Utilized this csv file to access additional set of songs, albums, danceability scores, spotify_url link, youtube_url link, & song duration.
    - These csv files were merged into a dataframe using Pandas to create data visualization bar graphs and access critical columns such as spotify_url links, youtube_url links, song duration, and a songs' danceability score. 
3. **.gitattributes**: Used to add spot_millsongdata.csv and Spotify_Youtube.csv to git
3. **filename2.txt**: This text file was created as a result of converting the merged dataframe of both csv files into a list of strings to allow our regex() function to parse through the strings and group them using regular expressions.
4. **spot_A_Song.py**: This python script was created to develop our game, "Spot-A-Song" which contains our Song class, functions, and methods to allow the user to type in the lyrics they want to search for in the prompt line and the artist (if applicable, but this step is optional) to produce their desired song or list of similar songs. Additionally, it provides the song's duration time, spotify link, youtube link in the console as well as the users' song's danceability score in the form of data visualization bar graph. 

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

Sources:

Mahajan, Shrirang. (2022, December 11). "Spotify Million Song Dataset." https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

Rastelli, Salvatore. (2023, March 11). "Spotify and Youtube." https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube

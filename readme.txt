
IMDB_Tagger

This program will search the video files in the given path by the user and Extract the movie_name/TV_Series_name from the file_name.based on this file name it scrape the IMDB rating from imdb.com and rename the file_name with the original file_name and rating tag.   

Instructions 

-->Install googleapiclient (sudo pip install --upgrade google-api-python-client)
-->Install Guessit (sudo pip install guessit)
-->Create google search API with your google account and get 'my_api_key'(https://developers.google.com/maps/documentation/maps-static/get-api-key) and 'my_cse_id'(https://cse.google.com/cse/create/new).While you are creating mention www.imdb.com site in the google console search.
-->ownload the archive and extract the .py file
-->paste your 'my_api_key' and 'my_cse_id' in the python code and save the file.
-->Open the terminal and type $python imdb_tagger.py
-->select the path of the movie or TV series Episode folder
-->Wait till it complete

What Happens
-->First you need to give your google api key and cse id.
-->when you first run the code, the script asks you to give the location of the folder in which the movies and series are loacted.
-->Then the script first selects the first file and checks whether there is an IMDb tag, if present it gives you response that the file has IMDb tag and goes to next file.
-->If the file doesn't have tag, then by using our both api keys we search for the movie/series name in IMDb site  and choose the first 10 results.
-->After this we convert the page into lxml format and we search for the rating value of the movie/series and then we scrape the data.
-->After getting the ratingvalue we rename the file name with IMDb rating(Example- Hera pheri[IMDD-8.2]) and gives the  output that the IMDb tag has been added to the file.

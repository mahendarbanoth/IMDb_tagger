IMDB_Rating_Tagger

This program will search the video files in the given path by the user and Extract the movie_name/TV_Series_name from the file_name.based on this file name it scrape the IMDB rating from imdb.com and rename the file_name with the original file_name and rating tag.   

 Instructions 

 1.If you didn't istalled pip
 	+This program file requires guessit, To install guessit and pip run the command in your terminal. 
 	- sudo apt-get install python-pip
 	- sudo pip install guessit
	- sudo pip install --upgrade google-api-python-client 
 2.Create google search API with your google account and get 'my_api_key'(https://developers.google.com/maps/documentation/maps-static/get-api-key) and 'my_cse_id'(https://cse.google.com/cse/create/new).While you are creating mention www.imdb.com site in the google console search.
 3.Download the archive and extract the .py file
 4.paste your 'my_api_key' and 'my_cse_id' in the python code and save the file.
 5.Open the terminal and type $python imdb_tagger.py
 6.select the path of the movie or TV series Episode folder
 7.Wait till it complete


Following takes place 
	1.Read all video files from the given path, stores the file_names in a list.
	2.Iterating throught each name in the list, sent a get request at IMDb site with the query file_name
	3.Scrape the IMBD rating from the result and tag to the orignal file_name.
	4.finally rename the file_name with the new name which has a IMDB rating.

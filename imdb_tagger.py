import urllib.request
import lxml
import lxml.html
import os
import re
import guessit
import fnmatch
import sys
import tkinter
import requests
from googleapiclient.discovery import build
from lxml import etree as ET
from guessit import guessit
from tkinter import filedialog

my_api_key = "my_api_key"
my_cse_id = "my_cse_id"
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


root = tkinter.Tk()
root.withdraw()
path = filedialog.askdirectory(parent=root, initialdir="/home/", title='Please select a Directory')
'''
print'Give the path where you have to search Example: /home/user/Desktop'
path=raw_input()
'''
files = os.listdir(path)

extensions = ("*.mp4", "*.webm", "*.avi", "*.mkv", "*.flv", "*.vob", "*.ogv", "*.ogg", "*.wmv","*.yuv", "*.rm", "*.rmvb", "*.asf", "*.amv", "*.mpeg", "*.svi", "*.3gp", "*.mxf", "*.flv")

for filename in files:
    for i in extensions:
        if fnmatch.fnmatch(filename, i):
            try:
                if re.search(r'[IMDB-[0-9].[0-9]]', filename):
                    print(filename+' already ADDED')
                else:
                    filedata = guessit(filename)

                    print(filedata['title'])
                    moviename = filedata['title']

                    if filedata['type'] == 'movie':
                        results = google_search(moviename, my_api_key, my_cse_id, num=10)
                        # print(results)

                    if filedata['type'] == 'episode':
                        episodename = filedata['episode_title']
                        print('Season- '+str(filedata['season']))
                        print('Episode- '+str(filedata['episode']))
                        results = google_search(moviename+' season ' + str(filedata['season'])+' episode ' + str(filedata['episode'])+' site:imdb.com/title', my_api_key, my_cse_id, num=10)

                    result = results[0]
                    # print(result)

                    link = result['htmlFormattedUrl']
                    site=requests.get(link)
                    root = lxml.html.fromstring(site.content)


                    lyrics_object_list = root.xpath('.//div[@id="quicklinksBar"]')

                    lyrics_object_rat = root.xpath('.//span[@itemprop="ratingValue"]/text()')
                    x=lyrics_object_rat[0]

                    filename_pref, filename_ext = os.path.splitext(filename)
                    new_filename = filename_pref+'['+'IMDB-'+x+']'+filename_ext

                    os.chdir(path)
                    os.rename(filename, new_filename)
                    print('IMDB rating added to '+filename)

            except Exception as e:
                print(e)
                print(filename+' got ERROR')

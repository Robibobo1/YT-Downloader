# importing the module
from importlib.resources import path
import os
from pickle import TRUE
from pytube import YouTube
from http.client import IncompleteRead
path = r'C:\Users\robin\Desktop\DAVID'

# where to save 
yt = YouTube("https://www.youtube.com/watch?v=fzvDI7XZ5vM&ab_channel=AngeMomoneetDavid")
dateObject = yt.publish_date
titre = yt.title
print(titre)
date = dateObject.strftime("%d-%m-%Y")
yt = yt.streams.get_highest_resolution()
yt.download(output_path = path,filename_prefix=date + " ")




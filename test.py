# importing the module
from pytube import YouTube
from http.client import IncompleteRead

# where to save
try: 
    YouTube("https://www.youtube.com/watch?v=y1MNj_LZ3aU&ab_channel=AngeMomoneetDavid").streams.get_highest_resolution().download()
except IncompleteRead:
    try:
        video = YouTube("https://www.youtube.com/watch?v=y1MNj_LZ3aU&ab_channel=AngeMomoneetDavid")
        res = video.streams.filter(progressive=True).get_by_resolution("480p")
        res.download()
    except:
        video = YouTube("https://www.youtube.com/watch?v=y1MNj_LZ3aU&ab_channel=AngeMomoneetDavid")
        res = video.streams.filter(progressive=True).get_by_resolution("360p")
        res.download()
    


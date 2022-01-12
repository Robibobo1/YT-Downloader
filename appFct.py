from pytube import YouTube
from pytube import Channel

def downloadNumber(nbrVideo,c):
    print("Telecharge " + str(nbrVideo) + " videos de la chaine: " + str(c.channel_name))
    x = 0
    for video in c.videos:
        highresvid = video.streams.get_highest_resolution()
        highresvid.download()
        print(highresvid)
        x = x + 1
        if x >= nbrVideo :
            break
    
    print("end")
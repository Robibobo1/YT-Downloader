# Import the required Librari
from pytube import YouTube
from pytube import Channel
from http.client import IncompleteRead


c = Channel('https://www.youtube.com/channel/UCF7hvVfLWDNuecBuhKxLjHA')
print("Télecharge toute les vidéos de la chaîne: " + str(c.channel_name) + r"")
for video in c.videos:
    try:
        highresvid = video.streams.filter(progressive=True).get_highest_resolution()
        print(highresvid.title.encode("utf-8"))
        print(highresvid)
        print("")
        highresvid.download(r'/mnt/Main_Pool/Media/BackupYoutube/David')
    except IncompleteRead:
        print(r"Erreur quelquonque, video de moins bonne qualite")
        try:
            video = YouTube("https://www.youtube.com/watch?v=y1MNj_LZ3aU&ab_channel=AngeMomoneetDavid")
            res = video.streams.filter(progressive=True).get_by_resolution("480p")
            res.download()
        except:
            video = YouTube("https://www.youtube.com/watch?v=y1MNj_LZ3aU&ab_channel=AngeMomoneetDavid")
            res = video.streams.filter(progressive=True).get_by_resolution("360p")
            res.download()
    

from pytube import YouTube
from pytube import Channel
from appFct import downloadNumber
    
print("Combien veux tu de videos ?")
userNumber = int(input())
ch = Channel('https://www.youtube.com/c/AngeMomoneetDavid2/videos')
downloadNumber(userNumber,ch)
# Import the required Libraries
import os
from tkinter import *
from pytube import YouTube
from pytube import Channel
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from turtledemo.colormixer import setbgcolor
from cgitb import grey

# Create an instance of tkinter frame
win = Tk()


# Set the geometry of tkinter frame
win.title("YT Channel Downloader")
win.geometry("500x330")

choice = IntVar()
channelAddr = ""

frame = Frame(master=win, width=500, height=330)
frame.pack()
         
btnStart = Button(master=frame,text="Start",width=25,height=2)
btnStart.place(x=30,y=165)

lblAdresse = Label(master=frame, text="Adresse de la chaîne: ")
lblAdresse.place(x=30,y=30)

txtAdresse = Entry(master=frame,width=50)
txtAdresse.insert(0,"https://www.youtube.com/channel/UCF7hvVfLWDNuecBuhKxLjHA")
txtAdresse.place(x=160,y=30)

lblDossier = Label(master=frame, text="Dossier d'installation: ")
lblDossier.place(x=30,y=60)

btnBrowse = Button(master=frame, text="Browse")
btnBrowse.place(x=160,y=57)

txtDossier = Entry(master=frame,width=40)
txtDossier.insert(0,r"C:\Users\robin\Desktop\DAVID")
txtDossier.place(x=220,y=60)

lblType = Label(master=frame,text="Type d'installation: ")
lblType.place(x=30,y=90)

radNbrVid = Radiobutton(master=frame,text="Nombre de vidéos",variable=choice,value=0)
radNbrVid.place(x=150,y=90)

txtNbrVid = Entry(master=frame,width=5,text="0")
txtNbrVid.insert(0,"1")
txtNbrVid.place(x=280,y=93)

radAll = Radiobutton(master=frame,text="Toute la chaîne",variable=choice,value=1)
radAll.place(x=150,y=120)
#print(choice.get())

lblStatus = Label(master=frame,bg="grey",width=25,height=2)
lblStatus.place(x=280,y=167)

lblConsole1 = Label(master=frame,text="-")
lblConsole1.place(x=30,y=220)

lblConsole2 = Label(master=frame,text="-")
lblConsole2.place(x=30,y=250)

lblConsole3 = Label(master=frame,text="-")
lblConsole3.place(x=30,y=280)

def main_fct():

    c = Channel(txtAdresse.get())
    lblStatus.config(bg="yellow")
    if choice.get() == 0:
        downloadNumber(c)
    if choice.get() == 1:
         downloadAll(c)
    
def open_file():
   file = filedialog.askdirectory()
   if file:
      txtDossier.insert(0, file)

    
def downloadNumber(c):
    lblConsole1.config(text="Télécharge " + txtNbrVid.get() + " vidéos de la chaîne: " + str(c.channel_name))
    x = 0
    for video in c.videos:
        date = video.publish_date.strftime("%d-%m-%Y")
        highresvid = video.streams.filter(progressive=True).get_highest_resolution()
        lblConsole3.config(text=highresvid)
        highresvid.download(output_path=txtDossier.get(),filename_prefix=date + " ")
        x = x + 1
        lblConsole2.config(text="Vidéos téléchargées: " + str(x))
        if x >= int(txtNbrVid.get()) :
            lblStatus.config(bg="green")
            break
          
def downloadAll(c):
    lblConsole1.config(text="Télecharge toute les vidéos de la chaîne: " + str(c.channel_name))
    x = 0
    for video in c.videos:
        date = video.publish_date.strftime("%d-%m-%Y")
        highresvid = video.streams.filter(progressive=True).get_highest_resolution()
        lblConsole3.config(text=highresvid)
        highresvid.download(output_path=txtDossier.get(),filename_prefix=date + " ")
        x = x + 1
        lblConsole2.config(text="Vidéos téléchargées: " + str(x))
    lblStatus.config(bg="green")
    
btnStart.config(command=main_fct)
btnBrowse.config(command=open_file)

win.mainloop()



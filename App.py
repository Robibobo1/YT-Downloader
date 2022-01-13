# Import the required Libraries
from appFct import downloadNumber
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from test.test_math import file
from turtledemo.colormixer import setbgcolor
from cgitb import grey

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("500x300")

choice = IntVar()
channelAddr = ""

frame = Frame(master=win, width=500, height=300)
frame.pack()
         
btnStart = Button(master=frame,text="Start",width=25,height=2)
btnStart.place(x=30,y=165)

lblAdresse = Label(master=frame, text="Adresse de la chaîne: ")
lblAdresse.place(x=30,y=30)

txtAdresse = Entry(master=frame,width=50)
txtAdresse.place(x=160,y=30)

lblDossier = Label(master=frame, text="Dossier d'installation: ")
lblDossier.place(x=30,y=60)

btnBrowse = Button(master=frame, text="Browse")
btnBrowse.place(x=160,y=57)

txtDossier = Entry(master=frame,width=40)
txtDossier.place(x=220,y=60)

lblType = Label(master=frame,text="Type d'installation: ")
lblType.place(x=30,y=90)

radNbrVid = Radiobutton(master=frame,text="Nombre de vidéos",variable=choice,value=0)
radNbrVid.place(x=150,y=90)

txtNbrVid = Entry(master=frame,width=5)
txtNbrVid.place(x=280,y=93)

radAll = Radiobutton(master=frame,text="Toute la chaîne",variable=choice,value=1)
radAll.place(x=150,y=120)
#print(choice.get())

lblStatus = Label(master=frame,bg="grey",width=25,height=2)
lblStatus.place(x=280,y=167)
lblStatus.config(bg="grey")

lblConsole1 = Label(master=frame,text="-")
lblConsole1.place(x=30,y=220)

lblConsole2 = Label(master=frame,text="-")
lblConsole2.place(x=30,y=250)

def main_fct():
    channelAddr = txtAdresse.get()
    lblConsole1.config(text=channelAddr)
    
def open_file():
   file = filedialog.askdirectory()
   if file:
      txtDossier.insert(0, file)

    
def downloadNumber(nbrVideo,c):
    lblConsole1.config(text="Telecharge " + str(nbrVideo) + " videos de la chaine: " + str(c.channel_name))
    x = 0
    for video in c.videos:
        highresvid = video.streams.get_highest_resolution()
        highresvid.download()
        print(highresvid)
        x = x + 1
        if x >= nbrVideo :
            break  
        
btnStart.config(command=main_fct)
btnBrowse.config(command=open_file)

win.mainloop()



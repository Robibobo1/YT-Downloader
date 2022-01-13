# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from test.test_math import file
from turtledemo.colormixer import setbgcolor
from cgitb import grey

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("500x250")

choice = IntVar()

def open_file():
   file = filedialog.askdirectory()
   if file:
      txtDossier.insert(0, file)
      
def main_fct():
    test = 0

frame = Frame(master=win, width=500, height=250)
frame.pack()

lblAdresse = Label(master=frame, text="Adresse de la chaîne: ")
lblAdresse.place(x=30,y=30)

txtAdresse = Entry(master=frame,width=50)
txtAdresse.place(x=160,y=30)

lblDossier = Label(master=frame, text="Dossier d'installation: ")
lblDossier.place(x=30,y=60)

Button(master=frame, text="Browse", command=open_file).place(x=160,y=57)

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

btnStart = Button(master=frame,text="Start",command=main_fct(),width=25,height=2)
btnStart.place(x=30,y=165)

lblStatus = Label(master=frame,bg="grey",width=25,height=2)
lblStatus.place(x=280,y=167)
lblStatus.config(bg="red")

win.mainloop()
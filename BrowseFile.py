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
win.geometry("700x350")

def open_file():
   #file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   file = filedialog.askdirectory()
   if file:
      print(file)


frame = Frame(master=win, width=300, height=300, bg="grey")

frame.pack()


label1 = Label(master=frame, text="I'm at (0, 0)", bg="red")

label1.place(x=0, y=0)


label2 = Label(master=frame, text="I'm at (75, 75)", bg="yellow")

label2.place(x=75, y=75)


# Add a Label widget
lblAdresse = Label(master=frame, text="Adresse de la chaîne: ")
lblAdresse.place(x=50,y=50)

# Create a Button
ttk.Button(master=frame, text="Browse", command=open_file).place(x=100,y=100)


win.mainloop()
import tkinter as tk

root = tk.Tk()

button = tk.Button(root,text="QUIT",command=quit)
button.pack(side=tk.LEFT)
label = tk.Label(root,text="Hello",)
label.pack(side=tk.RIGHT)
root.mainloop()
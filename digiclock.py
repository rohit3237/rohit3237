from tkinter import *
from tkinter.ttk import *

from time import strftime as strf

root = Tk()
root.title("Digital Clock")

def time():
    string = strf('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("mildest", 100), background = "blue", foreground = "#fff")
label.pack(anchor='center')
time()

mainloop()

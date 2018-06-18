# imports libs

import time
import tkinter
import Tkinter
from tkinter import Tk,PhotoImage
root =Tk()
root.title("Title")
root.geometry("600x600")
root.configure(background="black")

background_image = PhotoImage(file="Background.gif")

background = Label(root, image=background_image, bd=0)
background.pack()

root.mainloop

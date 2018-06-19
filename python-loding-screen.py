# imports libs
import sys
import os

import time
from tkinter import Tk, Label, Button
# main gui


class Mainscreen:
    def __init__(self, master):
        self.master = master
        master.title("Python Game")
        self.label = Label(master, text="Python_Game")
        self.label.pack()

        self.greet_button = Button(master, text="Start", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        os.system('python main.py')


root = Tk()
my_gui = Mainscreen(root)
root.mainloop()

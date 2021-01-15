"""
this is a very simple text editor written in python3
you will see two values used throughout
'0.0' = left zero is line zero, right is column zero
'END' = end of file
together this captures the entire screen of text
logging is also a feature of this program
logger -> texteditor.log

"""

import logging
import tkinter as tk
from tkinter.filedialog import *
from tkinter import messagebox as mb

filename = None

logging.basicConfig(filename='texteditor.log', filemode='w', level=logging.INFO)
logging.info('Program Started')


def newFile():
    global filename
    filename = 'Untitled'
    text.delete(0.0, tk.END)


def openFile():
    try:
        f = askopenfile(mode='r')
        t = f.read()
        text.delete(0.0, tk.END)
        text.insert(0.0, t)
    except Exception as err:
        logging.error(str(err))


def saveFile():
    global filename
    try:
        t = text.get(0.0, tk.END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except Exception as err:
        mb.showerror('Something went wrong saving the file')
        logging.error(str(err))


def saveAs():
    f = asksaveasfile(mode='w')
    t = text.get(0.0, tk.END)
    f.write(t.rstrip())


def About():
    mb.showinfo(title='About', message='A Very Simple Text Editor written in Python3\nusing the tkinter module')


root = tk.Tk()
root.title("Python Text Editor")
root.wm_iconbitmap('img/windows.ico')
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
text = Text(root, width=400, height=400)
text.pack()

menu = tk.Menu(root)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open...", command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.config(menu=menu)
tk.mainloop()

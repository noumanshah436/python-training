from tkinter import *


window = Tk()  # instantiate an instance of a window
window.geometry("420x420")             # set size of window
window.title("GUI program")

icon = PhotoImage(file='../logo.png')
window.iconphoto(True, icon)
window.config(background="grey")
# window.config(background="#5cfcff")

window.mainloop()  # place window on computer screen, listen for events


# ****************************************
# Tkinter(Tk_inter) is the standard GUI library for Python.
# Python when combined with Tkinter provides a fast and easy  way to create GUI applications.
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit
# ************
# widgets = GUI elements: buttons , textboxes, labels , images
# windows = serves as a container to hold or contain these widgets
# ************

# notes = 27. Python 3 – GUI Programming (Tkinter) ( page 428, content pg 12)
# D:\Python Notes\Python Notes\Python-Programming123uo00es0463.pdf

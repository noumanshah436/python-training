from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='../forward.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00ff00",
                bg="black",
                activeforeground="red",   # color when click
                activebackground="yellow",
                state=ACTIVE,     # state can be active or disabled
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()
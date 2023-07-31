from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='../logo2.png')
# photo = PhotoImage(file='C:\\Users\\Syed Numan Rehman\\Desktop\\logo.png')


label = Label(window,
              text="Hello",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',    # foreground color
              bg='black',      # background color
              relief= GROOVE,  # set border (flat, groove, raised, ridge, solid, or sunken)
              bd=10,          # border size
              padx=20,        # left/right padding
              pady=20,        # top/bottom padding
              image=photo,
              compound='bottom'  # where to place image relative to the text
              )
label.pack()
#label.place(x=0,y=0)

window.mainloop()

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Message Box')
root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")
root.geometry('400x400')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]    

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
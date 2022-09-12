from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Message Box')
root.iconbitmap("Image_Folder/icon.ico")
root.geometry('400x400')

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Would you like to supersize your order?", variable=var, onvalue="Yes", offvalue="No")
c.deselect()
c.pack()


myButton = Button(root, text="Show selection", command=show).pack()
root.mainloop()
from tkinter import *
import tkinter
from PIL import ImageTk, Image

root = Tk()
root.title('Message Box')
root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")

def open():
    global my_img
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")
    lbl = Label(top, text='hello!').pack()
    my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Samsung\Desktop\General\Projects\Python learning\Python Notes\Tkinter - PracticeFolder\Image_Folder\yellow_stone.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='close window',command=top.destroy).pack()

btn = Button(root, text='Open second window', command=open).pack()

root.mainloop()
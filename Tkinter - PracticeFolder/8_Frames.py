from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap("Image_Folder/icon.ico")

# frame = LabelFrame(root, text='This is my frame...', padx= 50, pady= 50)
frame = LabelFrame(root, padx= 50, pady= 50)
frame.pack(padx=100,pady=100)

b = Button(frame, text="Don't click here")
b2 = Button(frame, text="and here...")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)
#Can use grid / pack in frame
root.mainloop()
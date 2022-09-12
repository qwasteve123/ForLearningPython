from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Message Box')
root.iconbitmap("Image_Folder/icon.ico")

def open():
    global my_img
    dir = "Image_Folder"
    root.filename = filedialog.askopenfilename(initialdir=dir, title='Select A File', filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    #Get file full path
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(root, text=root.filename).pack()
    my_image_label = Label(root, image=my_img).pack()

my_btn = Button(root, text="Open File",command=open).pack()

root.mainloop()
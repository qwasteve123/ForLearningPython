from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap("Image_Folder/icon.ico")

# showinfo, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showerror("This is my popup!","Hello world")
    Label(root, text=response).pack()

    # For showinfo, showerror return 'ok'

    # For askyesno, askokcancel
    if response == 1:
        Label(root,text='you clicked yes').pack()
    elif response == 0:
        Label(root, text='you clicked no').pack()

    # For askquestion
    if response == 'yes':
        Label(root,text='you clicked yes').pack()
    elif response == 'no':
        Label(root, text='you clicked no').pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()


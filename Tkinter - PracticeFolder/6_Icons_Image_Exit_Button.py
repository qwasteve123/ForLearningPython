from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn python')
#Icon on window
#root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")

my_img = ImageTk.PhotoImage(Image.open(r"C:\......\watame.png"))
my_label = Label(image=my_img)
my_label.pack()

#Exit button
button_quit = Button(root, text="Exit program", command = root.quit)
button_quit.pack()

root.mainloop()
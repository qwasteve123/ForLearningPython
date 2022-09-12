from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap("Image_Folder/icon.ico")

#Let variable get values from elements
r = IntVar()
#r = Strar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in MODES:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()

myButton = Button(root, text='Click Me!',command=lambda:clicked(pizza.get()))
myButton.pack()

mainloop()
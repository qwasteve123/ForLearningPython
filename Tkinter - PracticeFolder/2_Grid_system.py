from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Steven")
myLabel3 = Label(root, text="                  ")
myLabel4 = Label(root, text="My name is Steven")


# #Grid System is relative, column = 5 will align with myLabel1
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)

myLabel2.grid(row=0, column=0)
myLabel3.grid(row=1, column=1)
myLabel4.grid(row=2, column=3)

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
# myLabel3.grid(row=2, column=3)
# myLabel4.grid(row=3, column=4)

root.mainloop()
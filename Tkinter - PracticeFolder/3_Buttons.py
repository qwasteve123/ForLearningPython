from tkinter import *

root = Tk()
''' Setting in Button widget
state = DISABLED prevent clicking button
state = DISABLED
____________________________________________
Button size
padx=50,pady=30
____________________________________________
Command
def myClick():
    myLAbel = Label(root, text="Click this button")
    myLAbel.pack()


myButton = Button(root, text= "Click me!", padx=50,pady=30, command = myClick())
____________________________________________
Text color, Button color
fg="blue"
bg="blue"

'''
def myClick():
    myLAbel = Label(root, text="Click this button")
    myLAbel.pack()


myButton = Button(root, text= "Click me!", padx=50,pady=30, command = myClick(),fg="blue",bg="#000000")
myButton.pack()
root.mainloop()
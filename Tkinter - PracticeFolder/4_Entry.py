from tkinter import *

'''Entry widget
1. Text, background color => bg="blue",fg="white" (color code or word)
2. Width, width=50
3. Border Width, borderwidth = 5
4. Get value of entry box, .get() method
5. Add words in Entry Box, .insert(0, "Your Text") method
'''

root = Tk()
e = Entry(root,width=50, borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name")


borderwidth = 5
def myClick():
    name = e.get()
    if name == "Jhon":
        greeting = "Hello, " + name
    else:
        greeting = name + ", I don't know you."

    myLAbel = Label(root, text=greeting)
    myLAbel.pack()

# No () in Button,command=
myButton = Button(root, text= "Enter your name", padx=50,pady=30, command = myClick)
myButton.pack()

myButton.pack()
root.mainloop()
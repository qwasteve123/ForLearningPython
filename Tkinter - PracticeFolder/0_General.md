# Tkinter Notes
## 1_Start a window
```python
from tkinter import *
root = Tk()
myLabel = Label(root, text="Hello World")

myLabel.pack()
root.mainloop()
```
## 2_Grid System

```python
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Steven")

#Grid System is relative, column = 5 will align with myLabel1
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
```
## 3_Button
```python
''' Setting in Button widget
myButton = Button(root, text= "Click me!", padx=50,pady=30, command = myClick)
state = DISABLED- prevent clicking button
padx=50,pady=30 -button size
fg, bg="blue" -color choice
'''
def myClick():
    myLAbel = Label(root, text="Click this button")
    myLAbel.pack()

myButton = Button(root, text= "Click me!", padx=50,pady=30, command = myClick(),fg="blue",bg="#000000")
myButton.pack()
```
## 4_Entry
```python
'''Entry widget
1. bg, fg
2. width=50
3. borderwidth = 5
4. .get() - Read input
5. .insert(0, "Your Text") - add words in entry box
'''
e = Entry(root,width=50, borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name")

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
```
## 5_Practical_Calcultor
```python
import math
from stat import FILE_ATTRIBUTE_NORMAL
from tkinter import *

root = Tk()
e = Entry(root,width=35, borderwidth = 5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0,END)    
    return

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0,END)    
    return

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0,END)    
    return

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0,f_num - int(second_number))

    if math == "multiplication":
        e.insert(0,f_num * int(second_number))

    if math == "division":
        e.insert(0,f_num / int(second_number))

button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))

button_add = Button(root,text="+",padx=30,pady=20,command=button_add)
button_subtract = Button(root,text="-",padx=30,pady=20,command=button_subtract)
button_multiply = Button(root,text="*",padx=30,pady=20,command=button_multiply)
button_divide = Button(root,text="/",padx=30,pady=20,command=button_divide)
button_equal = Button(root,text="Equal",padx=30,pady=20,command=button_equal)
button_clear = Button(root,text="Clear",padx=30,pady=20,command=button_clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=1,columnspan=1)
button_clear.grid(row=4, column=2,columnspan=1)

root.mainloop()
```
## Icons, Images, Exit Buttons
```python
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('image viewer')
root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")

dir_str = r"C:\Users\Samsung\Desktop\General\Projects\Python learning\Python Notes\Tkinter - PracticeFolder\Image_Folder"

my_img1 = ImageTk.PhotoImage(Image.open(dir_str +r"\1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(dir_str +r"\2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(dir_str +r"\3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open(dir_str +r"\4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open(dir_str +r"\5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=image_list[0])
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward = Button(root, text='>>', command=lambda:forward(image_number + 1))
    button_back = Button(root, text ="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text='>>', state=DISABLED)

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward = Button(root, text='>>', command=lambda:forward(image_number + 1))
    button_back = Button(root, text ="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text ="<<", command=lambda:back(1))
button_exit = Button(root, text="Exit Program", command = root.quit)
button_forward = Button(root, text='>>', command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
```
## 8_Frame
```python
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")

# frame = LabelFrame(root, text='This is my frame...', padx= 50, pady= 50)
frame = LabelFrame(root, padx= 50, pady= 50)
frame.pack(padx=100,pady=100)

b = Button(frame, text="Don't click here")
b2 = Button(frame, text="and here...")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)
#Can use grid / pack in frame
root.mainloop()
```
## 9_Radio_Buttons
```python
from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk, Image

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")

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
```
## 10_Message_Box
```python
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap(r"C:\Users\Samsung\Desktop\game.ico")

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
```
## 11_Create_New_Window
```python
from email.mime import image
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
```

from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime
from threading import *

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)
    
def addtolist():
    entrytxt = entry1.get()
    if check4dup() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0, END)
    
def addtolist2(event):
    entrytxt = entry1.get()
    if check4dup()==False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0, END)
    
def clearlist(event):
    listbox1.delete(0, END)
    findsize()
    
def clearlist2():
    listbox1.delete(0, END)
    findsize()
        
def check4dup():
    names = listbox1.get(0, END)
    if entry1.get() in names:
        return True
    else: 
        return False

def findsize():
    label1.config(text=listbox1.size())
    
def openfileR():
    clearlist2()
    f = open("Readme.txt", "r")
    for line in f:
        name = line[0:-1]
        listbox1.insert(END, name)
    f.close()
    findsize()
    
def openfileW():
    f= open("Readme.txt", 'w')
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")
    
    f.close()
    
d=datetime.now()
print d
y= d.year
print y

def generate():
    while(1):
        print "Hello"
        
thread1 = Thread(target=generate)
#thread1.start()
          
                            

root = Tk() #gives us a blank canvas object to work with
root.title("My GUI program with Tkinter.")

button1 = Button(root, text="Button 1", command=addtolist)
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>",addtolist2 )

label1 = Label(root, text="Hello World", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)


scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=1, column=2, rowspan=10, sticky=NS)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW, rowspan=10)
listbox1.bind("<Button-3>", clearlist)

#listbox1.insert(END, "Bob")
#listbox1.insert(END, "John")
#listbox1.insert(END, "Mary")

findsize()

image = Image.open("ball.jpg")
image = image.resize((100, 90))
photo = ImageTk.PhotoImage(image)

label2= Label(image=photo)
label2.image = photo #keep reference
label2.grid(row=7, column=1)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

mainloop() #causes the windows to display on the screen until program closes
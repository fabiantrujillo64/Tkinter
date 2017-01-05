from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)
    
def addtolist():
    entrytxt = entry1.get()
    listbox1.insert(END, entrytxt)
    entry1.delete(0, END)
    
def addtolist2(event):
    entrytxt = entry1.get()
    listbox1.insert(END, entrytxt)
    entry1.delete(0, END)
    
def clearlist(event):
    listbox1.delete(0, END)


root = Tk() #gives us a blank canvas object to work with
root.title("My GUI program with Tkinter.")

button1 = Button(root, text="Button 1", command=addtolist)
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>",addtolist2 )

label1 = Label(root, text="Hello World", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

listbox1 = Listbox(root)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW)
listbox1.bind("<Button-3>", clearlist)

listbox1.insert(END, "Bob")
listbox1.insert(END, "John")
listbox1.insert(END, "Mary")

mainloop() #causes the windows to display on the screen until program closes
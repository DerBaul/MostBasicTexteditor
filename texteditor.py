import sys
from tkinter import *
from tkinter import filedialog



root = Tk("Text Editor")
text=Text(root)
text.grid()

def saveas():
    global text
    t = str(text.get(1.0, END))
    file1 = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file1 == None:
        return
#    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text="Save", command=saveas)
button.grid()

root.mainloop()
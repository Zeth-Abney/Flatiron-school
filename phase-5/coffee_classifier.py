import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
import tkinterDnD
from PIL import Image,ImageTk

# create the main window
root = tkinterDnD.Tk()

# set the title of the window
root.title("Coffee Roast Classifier")

# set the size of the window
root.geometry("400x300")

stringvar = tk.StringVar()
stringvar.set('Drop here or drag from here!')


def drop(event):
    # This function is called, when stuff is dropped into a widget
    stringvar.set(event.data)

def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")

# With DnD hook you just pass the command to the proper argument,
# and tkinterDnD will take care of the rest
# note: You need a ttk widget to use these arguments

label_1 = ttk.Label(root, ondrop=drop, ondragstart=drag_command,
                    textvar=stringvar, padding=50, relief="solid")
label_1.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
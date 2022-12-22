from tkinter import *
import tkinter 
master=Tk()

def mkentry(parent,caption,width=None,**options):
    Label(parent,text=caption).pack(side=LEFT)
    entry=Entry(parent,**options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry
user=mkentry(master,"username:",10)
pswd=mkentry(master,"password:",10,show="*")
content=StringVar()

entry=Entry(master,textvariable=content)

entry.focus_set()


def cb():
    text=content.get()
    content.set(text)
    print(text)
butt=Button(master,text="submit",command=cb)
butt.pack(side=LEFT)
mainloop()
    

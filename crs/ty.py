from tkinter import *
from tkinter import messagebox
master=Tk()
##def me(parent,caption,width=None,**options):
##    Label(parent,text=caption).pack(side=LEFT)
##    entry=Entry(parent,**options)
##    if width:
##        entry.config(width=width)
##    entry.pack(side=LEFT)
##    return entry
##user=me(master,"username:",10)
##pswd=me(master,"password:",10,show="*")
##content=StringVar()
##e=Entry(master,textvariable=content)
##text=content.get()
##content.set(text)
####e=Entry(master)
##e.pack()
##e.focus_set()
##def cb():
##    print(e.get())
##b=Button(master,text="get",width=10,command=cb)
##b.pack()
####e=Entry(master,width=50)
##e.pack()
##text=e.get()
##
##
##mainloop()
##
user=["meg","shree"]
pswd=["1234","3456"]
x=Label(master,text="username").pack()
y=Label(master,text="password").pack()
e1=Entry(master)
e2=Entry(master)
def read_entry():
    us=e1.get()
    ps=e2.get()
    for i in range(len([user,pswd])):
        if (us!=:
            messagebox.showinfo("invalid username or password")
        
        
b1=Button(master,text="submit",width=10,command=read_entry)

e1.pack()
e2.pack()
b1.pack()

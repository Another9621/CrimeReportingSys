from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
from update import *    
    
def user(root):
    root.destroy()
    global master
    master=Tk()
    master.resizable(width=False, height=False)
    UFrame=Frame(master)
    UFrame.columnconfigure(0,weight=1)
    UFrame.rowconfigure(0,weight=1)
    UFrame.grid(column=0,row=0,sticky=(N,W,E,S))
    UFrame.pack(pady=100,padx=100)
    print('list of current user ids :',UID)
    master.title("crime reporting system")
    TitleLbl=Label(UFrame,text="Login Page For Registered Users ",fg='cyan',bg='black').grid(row=1,column=2)
    ULbl=Label(UFrame,text="Username")
    PLbl=Label(UFrame,text="Password")
    UTxt=Entry(UFrame)
    PTxt=Entry(UFrame)
    bullet="\u2022"
    PTxt.config(show=bullet)

    
    def cef():
        user=UTxt.get()
        pwd=PTxt.get()
        userlist=list(UID.keys())
        pwdlist=list(UID.values())
        for ID in UID:
            if user==ID and pwd==UID[ID]:
                newwin=Tk() #if succesfully logged in opens another page which does further formalities.
               
            elif (user not in userlist) :
                    
                messagebox.showinfo("","invalid username or ")
                
                break
            elif (pwd not in pwdlist):
                messagebox.showinfo("","invalid username or password")
                
                break

    SubmitBt=Button(UFrame,text="Submit",command=cef)
    regBt=Button(UFrame,text="Sign Up",command=signup)
##    b.place(relx = 0.6,rely=0.5, anchor = CENTER) 
##    x.place(relx=0.4,rely=0.3,anchor=NW)
##    g.place(relx=0.6,rely=0.3,anchor=NW)
##    h.place(relx=0.6,rely=0.35,anchor=NW)
##    y.place(relx=0.4,rely=0.35,anchor=NW)
    ULbl.grid(row=2,column=1)
    UTxt.grid(row=2,column=2)
    PLbl.grid(row=3,column=1)
    PTxt.grid(row=3,column=2)
    SubmitBt.grid(row=4,column=2)
    RegLbl=Label(UFrame,text="Not registered yet?? Create your own User Id. Click on Sign Up").grid(row=5,column=2)
    regBt.grid(row=6,column=2)
##    signup.mainloop()
##    reg.pack()
    master.mainloop()
##user()


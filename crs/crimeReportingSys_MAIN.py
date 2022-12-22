
from tkinter import messagebox
from user_login import *
from admin_login import *
from guest_user import *
from Logger import *

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root. title('CRS: Crime Reporting System')
var=IntVar()

def sel1():
    selection='you selected the admin'
    label.config(text=selection)
def sel2():
    selection='you selected the user '
    label.config(text=selection)
def sel3():
    selection='you selected the guest user'
    label.config(text=selection)

## fUNCTION THAT CREATES NEW WINDOWS DEPENDING ON THE LOGIN CHOSEN BY USER    
def new_winF():
    if(var.get()==1):
        log('admin user selected.\nCalling Admin module') 
        admin(root)
    elif (var.get()==2):
        user(root)
    elif (var.get()==3):
        guest_user(root)
    else:
        display = Label(root, text=" please select  user",fg='red',bg='black')
        display.pack()

## END OF NEWWINF FUNCTION

## CODE FOR DISPLAYING CRS LOGO
img1=Image.open('crslogo.jpg')
Img=ImageTk.PhotoImage(img1)
w=img1.width
h=img1.height
Imgframe=Frame(root)
Imgframe.pack(anchor=CENTER,padx=50,pady=50)
lbl=StringVar()
lbl.set('Welcome!')
Lbl=Label(Imgframe,image=Img,textvariable=lbl,height=h,width=w)
Lbl.grid(row=1,column=2)

## CODE FOR DISPLAYING LOGIN CHOICES TO USER THROUGH RADIO BUTTONS
r1=Radiobutton(Imgframe,text='admin',fg='red',variable=var,value=1,command=sel1)
r1.grid(row=2,column=1)
r2=Radiobutton(Imgframe,text='user',fg='blue',variable=var,value=2,command=sel2)
r2.grid(row=2,column=2)
r3=Radiobutton(Imgframe,text='guestuser',fg='green',variable=var,value=3,command=sel3)
r3.grid(row=2,column=3)

label=Label(Imgframe)
label.grid(row=3,column=2)

b1=Button(Imgframe,text="LOGIN",command=new_winF)
b1.grid(row=4,column=2)
openlog()
log('CRS.py executed')
root.mainloop()

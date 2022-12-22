from tkinter import *
import tkinter

master=Tk()

box1=Label(master,text='X!!',fg='red',bg='black')
##data=Entry(master,textvariable=content)
##name.pack(padx=100,pady=20)
box1=Label(master,text='1',fg='red',bg='black')
box2=Label(master,text='2',fg='red',bg='black')

box3=Label(master,text='3',fg='red',bg='black')

box4=Label(master,text='4',fg='red',bg='black')

box5=Label(master,text='5',fg='red',bg='black')

box6=Label(master,text='6',fg='red',bg='black')
box1.grid(row=0,column=0,padx=10,pady=10)
box2.grid(row=0,column=1,padx=10,pady=10)
box3.grid(row=1,column=0,padx=10,pady=10)
box4.grid(row=1,column=1,padx=10,pady=10)
box5.grid(row=2,column=0,padx=10,pady=10)
box6.grid(row=2,column=1,padx=10,pady=10)

data=Entry(master)
PwdTxt=Entry(master,show='\u2022')
data.grid(row=3,column=1)
PwdTxt.grid(row=3,column=1)
mainloop()

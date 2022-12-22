    
import mysql.connector as mc
from testing import *
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk,Image
from Logger import *
data=tuple()
class megha(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initialize_user_interface()
    def initialize_user_interface(self):
        self.parent.title("List of cases")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")
        self.butt1=Button(self.parent,text="exit",command=self.parent.destroy).grid(row=0,column=4)
        self.tree=Treeview(self.parent,columns=("c_type","date_incident","descr"))
        self.tree.heading("#0",text="sno")
        self.tree.heading("#1",text="c_type")
        self.tree.heading("#2",text="date_incident")
        self.tree.heading("#3",text="descr")
        self.tree.column("#1",stretch=YES)
        self.tree.column("#2",stretch=YES)
        self.tree.column("#3",stretch=YES)
        self.tree.column("#0",stretch=YES)
        self.tree.grid(row=5,columnspan=4)
        self.treeview=self.tree
        self.i=0

    def  insert_data(self):
        log('entered insert_ data function in class megha for creatign table')
        global data
        for rec in data:
            self.treeview.insert("","end",text=str(self.i),values=rec)
            self.i=self.i+1
        print(data)
        


def guest_user(root):
    root.destroy()
    master=Tk()
    
    l=Label(master,text="window for guest users",font='algerian',fg='maroon')
   
    l.pack(pady=50)
    #logo display code
    img1=Image.open('crslogo_tile.jpg')
    Img=ImageTk.PhotoImage(img1)
    w=img1.width
    h=img1.height
    lbl=StringVar()
    lbl.set('Welcome!')
    Lbl=Label(master,image=Img,textvariable=lbl,height=h,width=w)
    Lbl.place(x=0,y=0,relwidth=1,relheight=1)
    Lbl.pack(anchor=CENTER,pady=10)
    Imgframe=Frame(master)
    Imgframe.pack(anchor=CENTER,padx=20,pady=10)

    
    mainframe=Frame(master)
    mycon=mc.connect(host="localhost",user="root",passwd="",database="user")
    cur=mycon.cursor()
    
    
    var=IntVar()
    def sel1():
        selection='you have opted to see cases in your locality'+str(var.get())
        label.config(text=selection)
    def sel2():
        selection='you selected the user option'+str(var.get())
        label.config(text=selection)
    def sel3():
        selection='you selected the guest user'+str(var.get())
        label.config(text=selection)
    def new_winF():
        log('inside new win function')
        if(var.get()==1):
            log('inside first checkbox condition')
            newwin = Toplevel(mainframe)
            l1=Label(newwin,text="enter the name of your locality").grid(row=1,column=1)
            l2=Label(newwin,text="enter your state").grid(row=2,column=1)
            e1=Entry(newwin)
            e2=Entry(newwin)
            def Chk():
                loc=e1.get()
                sta=e2.get()
                st="select c_type,date_incident,descr from cases where locality='%s' and state='%s';" %(loc,sta)
                log("query being executed::",st)
                cur.execute(st)
                global data
                data=cur.fetchall()
                log(data)
                d=megha(newwin)
                d.insert_data()
            e1.grid(row=1,column=2,padx=5,pady=5)
            e2.grid(row=2,column=2,padx=5,pady=5)
            SeeBt=Button(newwin,text="See Cases",command=Chk).grid(row=3,column=1,padx=20,pady=10)

            
        elif (var.get()==2):
            newwin = Toplevel(mainframe)
            query="select distinct locality from cases ;"
            cur.execute(query)
            locality=cur.fetchall()
            log('locality:',locality)
            for area in locality:
                st1="select c_type, count(c_type) from cases where locality='%s' group by c_type order by count(c_type)  desc;" %(area)
                log('query executed is:',st1)
                cur.execute(st1)
                data1=cur.fetchall()
                log (data1)
                rec =data1[0]
                log('rec:',rec)
                caption='Most prevalent crime in '+str(area[0])+' is '+rec[0]+'--- '+str(rec[1])+'  cases'
                log(caption)
                x=Label(newwin,text=caption,font='Arial',fg='red')
                x.pack(padx=20,pady=20)
        elif (var.get()==3):
            log("insert chart")
            crimes=[]
            stats=[]
            st2="select count(c_type),c_type from cases group by c_type;"
            cur.execute(st2)
            dat=cur.fetchall()
            log(dat)
            for item in dat:
                    stats.append(item[0])
                    crimes.append(item[1])
            log(crimes)
            log(stats)
            plot=plt.pie(stats,labels=crimes)
            plt.title('Crime Statistics')
            plt.show()
            plt.savefig('piechart.jpg')
        else:
            newwin = Toplevel(mainframe)
            display = Label(newwin, text=" please select  user",fg='black')
            display.pack()
            master.destroy()
    r1=Checkbutton(mainframe,text='SHOW NEARBY CASES',variable=var,onvalue=1,command=sel1)
    r1.pack(anchor=W)
    r2=Checkbutton(mainframe,text='Most Prevalent Crimes',variable=var,onvalue=2,command=sel2)
    r2.pack(anchor=W)
    r3=Checkbutton(mainframe,text='Statistics',variable=var,onvalue=3,command=sel3)

    r3.pack(anchor=W)
    label=Label(mainframe)
    label.pack()
    b1=Button(mainframe,text="submit",command=new_winF)
    b1.pack()

    mainframe.pack(padx=50,pady=20)
    mainframe.mainloop()        




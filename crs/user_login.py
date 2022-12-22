from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
from update import *    
from fir import *
from PIL import ImageTk,Image
from Logger import *
## Login page for users
def user(root):
        log('inside user function in user login module')
        log('list of current user ids :',UID)
        root.destroy()

        global master
        master=Tk()
        master.resizable(width=False, height=False)       
        master.title("crime reporting system")

        #code to display project logo
        img1=Image.open('crslogo_tile.jpg')
        Img=ImageTk.PhotoImage(img1)
        w=img1.width
        h=img1.height
        lbl=StringVar()
        lbl.set('Welcome!')
        Imgframe=Frame(master)
        Imgframe.grid(column=0,row=0,sticky=(N,W,E,S),pady=20,padx=20)
        Lbl=Label(Imgframe,image=Img,textvariable=lbl,height=h,width=w)
##        Lbl.place(x=0,y=0,relwidth=1,relheight=1)
        Lbl.pack(anchor=CENTER,padx=10,pady=10)

        UFrame=Frame(master)
        UFrame.columnconfigure(0,weight=1)
        UFrame.rowconfigure(0,weight=1)
        UFrame.grid(column=0,row=1,sticky=(N,W,E,S),pady=20,padx=20)
        TitleLbl=Label(UFrame,text="Login Page For Registered Users ",fg='cyan',bg='black').grid(row=1,column=2,pady=10)
        ULbl=Label(UFrame,text="Username")
        PLbl=Label(UFrame,text="Password")
        UTxt=Entry(UFrame)
        PTxt=Entry(UFrame)
        bullet="\u2022"
        PTxt.config(show=bullet)

        # function to authenticate user id and open new window for correct login
        def cef():
                log('inside cef function: Submit button was clicked for user login')
                user=UTxt.get()
                pwd=PTxt.get()
                userlist=list(UID.keys())
                pwdlist=list(UID.values())
                if user in UID and pwd==UID[user]:
                        newwin=Tk() #if succesfully logged in opens another page which does further formalities.
                        log('user id and pwd matched')
                        newwin.title('USER DashBoard')
                        master.destroy()
                        def destroy():
                                newwin.destroy()
                        def Reg():
                            fir(user)
                        #function to show status of user's cases
                        def Show_stat():
                            log('inside show_stat function: SHOW CASE STATUS Button was pressed')
                            InfoLbl=Label(newframe,text=user+", to view freshly registered complaints please log out and log in again ",fg='yellow',bg='red').grid(row=1,column=2,padx=20,pady=20)
                            query="select caseno,case_status from cases where userid='%s';" %(user)
                            mycur.execute(query)
                            log("query being executed::",query)
                            res=mycur.fetchall()
                            columns=mycur.column_names
                            log('result of query:\n', res)
                            ## prapring data for display
                            text=Text(newframe)
                            text.delete('1.0',END)
                            text.config(height=len(res)+1,width=50,wrap=WORD)
                            data_rec={}
                            for col in (columns):
                                text.insert(END,col+'\t ')
                            text.insert(END,'\n ')                        
                            for  rec in res:
                                text.insert(END,str(rec[0])+'\t'+str(rec[1])+'\n')
                            text.grid(row=2,column=2)
                            newframe.pack(padx=50,pady=50)
                        #end of show_stat function
                            
                        newframe=Frame(newwin)
                        Welcome=Label(newwin,text="Welcome "+user,fg='yellow',bg='green').pack(padx=50,pady=50)
                        CloseBt=Button(newwin,text="CLOSE",command=destroy).pack()
                        ShowBt=Button(newwin,text="SHOW CASE STATUS",command=Show_stat).pack()
                        MgrBt=Button(newwin,text="REGISTER COMPLAINT",command=Reg).pack()
                        
                        
                        newwin.mainloop()

                        #end of if block for successful login
                elif (user not in userlist) :                
                        messagebox.showinfo("","invalid username or ")
                elif (pwd not in pwdlist):
                    messagebox.showinfo("","invalid username or password")
# end of cef function
        SubmitBt=Button(UFrame,text="Submit",command=cef)
        regBt=Button(UFrame,text="Sign Up",command=signup)
        ULbl.grid(row=2,column=1,padx=10,pady=10)
        UTxt.grid(row=2,column=2,padx=10,pady=10)
        PLbl.grid(row=3,column=1,padx=10,pady=10)
        PTxt.grid(row=3,column=2,padx=10,pady=10)
        SubmitBt.grid(row=4,column=2,padx=10,pady=10)
        RegLbl=Label(UFrame,text="Not registered yet?? Create your own User Id. Click on Sign Up").grid(row=5,column=2,padx=10,pady=10)
        regBt.grid(row=6,column=2,padx=10,pady=10)
        def destroy():
             master.destroy()
        CloseBt=Button(UFrame,text="CLOSE",command=destroy).grid(row=6,column=3,padx=10,pady=10)


        master.mainloop()
##user()


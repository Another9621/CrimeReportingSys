from tkinter import *
from tkinter import messagebox
from update import *
import mysql.connector as mc
from PIL import ImageTk,Image
from Logger import *
## function to get case information from DB and get case details
## this function is called when view button is clicked
def show():
        log('Inside show function: VIEW Button was clicked')
        global cases
        Sel_case=cases.get()
        log('the selected case is',Sel_case)
        query='select * from cases where caseno='+cases.get()+'; '
        log('query executed',query)
        mycur.execute(query)
        res=mycur.fetchall()
        columns=mycur.column_names
        rec=res[0]

## prapring data for display
        global text
        text.delete('1.0',END)
        text.config(height=len(columns),width=50,wrap=WORD)
        data_rec={}
        for index in range(len(columns)):
                data_rec[columns[index]]=rec[index]
        log(data_rec)
        for  key in data_rec:
                text.config(fg='green')
                text.insert(END,str(key)+':  ')
                text.insert(END,str(data_rec[key])+'\n')
        text.pack(anchor=CENTER)
## END OF SHOW FUNCTION        
      
## Cur select function allows admin user to access and update case details
def CurSelect():
        log('inside cur select function: show cases Button was clicked')
        global root2
        global text
        text=Text(root2)
         
## fetching case info from case table
        mycur.execute("select caseno from cases;")
        log('Query executed: select caseno from cases;')
        data=mycur.fetchall()
        caselist=[]
        for rec in data:
                caselist.append(rec[0])
        log("cases in table:",caselist)
        global cases
        cases=StringVar(root2)
        global Mainframe
        Mainframe=Frame(root2)
        Mainframe.pack(pady=50,padx=50)
        Choice=Label(Mainframe,text="Choose from cases listed below").grid(row=1,column=2)
##displaying case no in drop down
        cases.set('caseno')
        CaseMenu=OptionMenu(Mainframe,cases,*caselist)
        CaseMenu.grid(row=2,column=2)
        
        ViewBt=Button(Mainframe,text="View",command=show).grid(row=3,column=1)                    
        UpdateBt=Button(Mainframe,text="Update",command=updating).grid(row=3,column=3)
# function to manage the userids. fucntion creates new window giving option to delete or create user, admin, change password,etc
def manageids():
        log('inside Manage ids function: Manage Users Button was clicked')
        global root2
        global Mainframe
        NewMgrwin=Tk()
        Mgrframe=Frame(NewMgrwin)
        Mgrframe.pack(pady=50,padx=50)
        #FUNCTION TO VALIDATE ADMIN PASSWORD AGAIN FOR SENSITIVE OPERATIONS
        def chk_adm(cmd):
             ReLbl=Label(Mgrframe,text="Re enter Admin Password").grid(row=5,column=1)
             RePwdTxt=Entry(Mgrframe)
             bullet="\u2022"
             RePwdTxt.config(show=bullet)
             def check():
                 Repwd=RePwdTxt.get()
                 if  Repwd!=pwd:
                         ErrLbl=Label(Mgrframe,text="Wrong Admin Password",fg='red',bg='white').grid(row=5,column=3)
                 else:
                         if cmd=='create':
                             signupadm()
                         elif cmd=='delete':
                             deleteadm(adm)
                         elif cmd=='password':
                                 change()
             RePwdBt=Button(Mgrframe,text="Check password",command=check).grid(row=6,column=2)        
             RePwdTxt.grid(row=5,column=2)
        #END OF CHK_ADM FUNCTION     
        def sign_adm():
            chk_adm('create')
        def del_adm():
            chk_adm('delete')
        def chg_pwd():
                chk_adm('password')
        def destroy():
                NewMgrwin.destroy()
        
        CUserBt=Button(Mgrframe,text="Create User",command=signup).grid(row=2,column=1,padx=5,pady=5)
        DUserBt=Button(Mgrframe,text="Delete User",command=del_user).grid(row=2,column=2,padx=5,pady=5)        
        CAdminBt=Button(Mgrframe,text="Create Admin",command=sign_adm).grid(row=3,column=1,padx=5,pady=5)  
        DAdminBt=Button(Mgrframe,text="Delete Admin",command=del_adm).grid(row=3,column=2,padx=5,pady=5)        
        PwdBt=Button(Mgrframe,text="Change password",command=chg_pwd).grid(row=4,column=1,padx=5,pady=5)
        ClsBt=Button(Mgrframe,text="Go Back",command=destroy).grid(row=4,column=2,padx=5,pady=5)

        NewMgrwin.mainloop()
## END OF MANAGE IDS FUNCTION

##main function that displays admin login page
def admin(root):
        log('inside admin function')
        root.destroy()
        global master
        master=Tk()
        master.resizable(width=False, height=False)
        log('list of current Admin ids :',AUID)
        mycur.execute("select * from cases;")
        data1=mycur.fetchall()
        master.title("CRS:Crime Reporting System -Admin Login")
        master.geometry("250x250")
        #code to display project logo
        img1=Image.open('crslogo.jpg')
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
        
        AdmLbl=Label(Imgframe,text="Admin User")
        PwdLbl=Label(Imgframe,text="Password")
        
        AdmTxt=Entry(Imgframe)
        PwdTxt=Entry(Imgframe)
        bullet="\u2022"
        PwdTxt.config(show=bullet)
        ## function called when admin user submits user id pwd; checks id pwd and calls next page
        def cef():
            log('within cef function: submit button for admin login was pressed')
            global adm,pwd
            adm=AdmTxt.get()
            pwd=PwdTxt.get()
            admList=list(AUID.keys())
            pwdList=list(AUID.values())
            for id in AUID:
                if adm==id and pwd==AUID[id]:
                        log('user id and pwd matched')
                        global root2
                        root2=Tk()
                        root2.title('ADMIN DashBoard')
                        master.destroy()
                        def destroy():
                                root2.destroy()
                        Welcome=Label(root2,text="Welcome "+adm,fg='yellow',bg='green').pack(padx=50,pady=50)
                        CloseBt=Button(root2,text="CLOSE",command=destroy).pack(padx=10,pady=10)
                        ShowBt=Button(root2,text="MANAGE CASES",command=CurSelect).pack(padx=10,pady=10)
                        MgrBt=Button(root2,text="MANAGE USER PROFILES",command=manageids).pack(padx=10,pady=10)
                        root2.mainloop()
                        break
                elif (adm not in AUID):
                        messagebox.showinfo("ERROR","invalid Userid")
                        break
                elif (pwd not in pwdList):
                        messagebox.showinfo("ERROR","invalid password")
                        break
            else: 
                    messagebox.showinfo("ERROR","invalid username ")
                    
        SubmitBt=Button(master,text="SUBMIT",command=cef)
        AdmLbl.grid(row=2, column=1,padx=5,pady=5)
        AdmTxt.grid(row=2, column=2,padx=5,pady=5)
        PwdLbl.grid(row=3, column=1,padx=5,pady=5)
        PwdTxt.grid(row=3, column=2,padx=5,pady=5)
        SubmitBt.place(x=0,y=0,relwidth=1,relheight=1)
        SubmitBt.pack( anchor = CENTER,pady=5)

        master.mainloop()
####
##Demo=Tk()
##admin(Demo)


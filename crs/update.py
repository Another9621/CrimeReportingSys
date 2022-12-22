import mysql.connector as mc
from tkinter import *
from tkinter import messagebox
from Logger import *

mycon=mc.connect(host="localhost",user="root",passwd="KVnlc123*",database="user")
mycur=mycon.cursor()
mycur.execute("select * from users where UType='user';")
User_rec=mycur.fetchall()
global UID
UID={}
for rec in  User_rec:
    UID[rec[0]]=rec[1]
mycur.execute("select * from users where UType='admin';")
Admin_rec=mycur.fetchall()
global AUID
AUID={}
for rec in  Admin_rec:
    AUID[rec[0]]=rec[1]

#function to update case status
##    -- opens a new window to get case no and case status from user
##    validates case no and updates case table with new case status
def updating():
    log('inside updating function: for updating cases status')
    root=Tk()

    case_stLbl=Label(root,text="case status")
    case_stTxt=Entry(root)
    caselist=[]
    case_noLbl=Label(root,text="case number")
    case_noTxt=Entry(root)
    mycur.execute("select * from cases;")
    data=mycur.fetchall()
    for rec in data:
        caselist+=[rec[0]]
    log('current case numbers in DB:',caselist)

    # update function, connects to DB to change case status
    def update():
        log('submit button pressed in update window')
        case_status=case_stTxt.get()
        log("case status:" ,case_status, type(case_status))
        caseno=case_noTxt.get()
        log("case no:" ,caseno, type(caseno))
        if (case_status =="") or (caseno =="" ) or (int(caseno) not in caselist):
            messagebox.showinfo("","enter caseno and case status before submitting")
        else:
            getstatus_stmt="select case_status from cases where caseno='"+caseno+"';"
            log("For fetching old status from DB: query being executed::\n",getstatus_stmt)
            mycur.execute(getstatus_stmt)
            oldstat=mycur.fetchall()
            oldstat=str(oldstat[0])
            oldstat=oldstat[2:-3]
            log('oldstatus:',oldstat)
            newcase_status=oldstat+'--'+case_status
            st="update cases set case_status='%s' where caseno='%s';"%(newcase_status,caseno)
            log("query being executed::",st)
            mycur.execute(st)
            mycon.commit()
            messagebox.showinfo("Success","Case Status updated in Database")
            
            root.destroy()
           
        log("End of update() function ")
       #end of update function     

    but=Button(root,text="SUBMIT",command=update).grid(row=3,column=1)
    case_noLbl.grid(row=1,column=1,padx=10,pady=10)
    case_noTxt.grid(row=1,column=2,padx=10,pady=10)
    case_stLbl.grid(row=2,column=1,padx=10,pady=10)
    case_stTxt.grid(row=2,column=2,padx=10,pady=10)
    def back():
            root.destroy()

    BackBt=Button(root,text="GO BACK",command=back).grid(row=3,column=2)

    root.mainloop()
## END OF UPDATING FUNCTION


##Sign up function for creating new user id            
def signup():
        log('connecting to DB to get existing user ids')
        sign_win=Tk()
        sign_win.title('CRS: Create New User ID')
        Signframe=Frame(sign_win)
        MainLbl=Label(Signframe,text="Create your User Id").grid(row=1,column=2)
        Signframe.pack(pady=10,padx=10)
        userLbl=Label(Signframe,text="Username").grid(row=2,column=1)
        userTxt=Entry(Signframe)
        pwdLbl=Label(Signframe,text="Password").grid(row=3,column=1)
        bullet="\u2022"     
        pwdTxt=Entry(Signframe)    
        pwdTxt.config(show=bullet)
        cpwdLbl=Label(Signframe,text="confirm ").grid(row=4,column=1)
        cpwdTxt=Entry(Signframe)

       #function to validate user id and create new user id
        def reg_user():
            newuserid=userTxt.get()
            newpwd=pwdTxt.get()
            cpwd=cpwdTxt.get()
            log('user entered values: uid: ',newuserid, 'pwd:',newpwd, '\nConfirm pwd:',cpwdTxt)
            if  newuserid in UID:
                log('user id already in dictionary')
                reenter=Label(Signframe,text=" User id already exists. re enter another id",fg='red',bg='white').grid(row=2,column=3)
            elif newpwd!=cpwd:
                log('Passwords dont match')
                repwd=Label(Signframe,text=" Passwords dont match!! Re enter password",fg='red',bg='white').grid(row=4,column=3)
            else:
                log('creating new user id')
                UID[newuserid]=newpwd
                log('connecting to DB to add new user')
                insert_stmt="insert into users values('"+newuserid+"','"+newpwd+"','user','new user');"
                log('QUERY TO BE EXECUTED:',insert_stmt)
                mycur.execute(insert_stmt)
                mycur.execute('commit;')
                log('new user added to user table')
                log('list of current user ids :',UID)
                messagebox.showinfo("ID Created!"," Your id has been created succesfully. \npress OK to LOG IN and continue",)
                sign_win.destroy()

##         Arranging display using grid   
        userTxt.grid(row=2,column=2)
        pwdTxt.grid(row=3,column=2)
        cpwdTxt.grid(row=4,column=2)
        SignBt=Button(Signframe,text="SIGN UP",command=reg_user).grid(row=5,column=1)
        def back():
            sign_win.destroy()

        BackBt=Button(Signframe,text="GO BACK",command=back).grid(row=5,column=2)
        
        sign_win.mainloop()
##end of signup function

##admin sign up function
def signupadm():
        sign_win=Tk()
        sign_win.title('CRS: Create Admin ID')
        Signframe=Frame(sign_win)
        MainLbl=Label(Signframe,text="Create your ADMIN Id").grid(row=1,column=2)
        Signframe.pack(pady=10,padx=10)
        userLbl=Label(Signframe,text="Username").grid(row=2,column=1)
        userTxt=Entry(Signframe)
        pwdLbl=Label(Signframe,text="Password").grid(row=3,column=1)
        bullet="\u2022"     
        pwdTxt=Entry(Signframe)    
        pwdTxt.config(show=bullet)
        cpwdLbl=Label(Signframe,text="confirm ").grid(row=4,column=1)
        cpwdTxt=Entry(Signframe)

       #function to validate user id and create new user id
        def reg_user():
            newuserid=userTxt.get()
            newpwd=pwdTxt.get()
            cpwd=cpwdTxt.get()
            log('user entered values: uid: ',newuserid, 'pwd:',newpwd, '\nConfirm pwd:',cpwdTxt)
            if  newuserid in AUID:
                log('user id already in dictionary')
                reenter=Label(Signframe,text=" User id already exists. re enter another id",fg='red',bg='white').grid(row=2,column=3)
            elif newpwd!=cpwd:
                log('Passwords dont match')
                repwd=Label(Signframe,text=" Passwords dont match!! Re enter password",fg='red',bg='white').grid(row=4,column=3)
            else:
                log('creating new admin id')
                UID[newuserid]=newpwd
                log('connecting to DB to add new admin')
                insert_stmt="insert into users values('"+newuserid+"','"+newpwd+"','admin','new admin');"
                log('QUERY TO BE EXECUTED:',insert_stmt)
                mycur.execute(insert_stmt)
                mycur.execute('commit;')
                log('new user added to user table')
                log('list of current admin ids :',AUID)
                messagebox.showinfo("ID Created!"," Your id has been created succesfully. \npress OK to LOG IN and continue",)
                sign_win.destroy()

##         Arranging display using grid   
        userTxt.grid(row=2,column=2)
        pwdTxt.grid(row=3,column=2)
        cpwdTxt.grid(row=4,column=2)
        SignBt=Button(Signframe,text="SIGN UP",command=reg_user).grid(row=5,column=1)
        def back():
            sign_win.destroy()

        BackBt=Button(Signframe,text="GO BACK",command=back).grid(row=5,column=2)
        
        sign_win.mainloop()
##end of signupadm function
        
##Function to delete admin user
def deleteadm(cur_user):
        del_win=Tk()
        del_win.title('CRS: Delete Admin')
        delframe=Frame(del_win)
        MainLbl=Label(delframe,text="Enter ADMIN Id (to be deleted)").grid(row=1,column=2)
        delframe.pack(pady=10,padx=10)
        userLbl=Label(delframe,text="Username").grid(row=2,column=1)
        userTxt=Entry(delframe)

       #function to validate user id and delete admin user id
        def dele():
            admid=userTxt.get()
            log('user entered values: uid: ',admid)
            if admid==cur_user:
                messagebox.showinfo("Invalid Operation!",admid+" You cannot delete your own id!!\n Login with other admin to delete this id!! ")
            elif  admid in AUID:
                log('admin id is present in dictionary')
                log('connecting to DB to delete admin')          
                del_stmt="delete from users where uid='"+admid+"' and UType='admin';"
                log('QUERY TO BE EXECUTED:',del_stmt)
                mycur.execute(del_stmt)
                mycur.execute('commit;')
                log('Admin user deleted from user table')
                del AUID[admid]
                log('list of current admin ids :',AUID)
                messagebox.showinfo("Admin ID deleted!",admid+"  has been deleted succesfully. ",)
                del_win.destroy()
            else:
                reenter=Label(delframe,text=" Admin User id does not exist. re enter correct id",fg='red',bg='white').grid(row=2,column=3)

##         Arranging display using grid   
        userTxt.grid(row=2,column=2)
        DelBt=Button(delframe,text="DELETE ADMIN",command=dele).grid(row=5,column=1)
        def back():
            del_win.destroy()

        BackBt=Button(delframe,text="GO BACK",command=back).grid(row=5,column=2)
        
        del_win.mainloop()
##end of del admin function

##Function to delete  user
def del_user():
        del_win=Tk()
        del_win.title('CRS: Delete User')
        delframe=Frame(del_win)
        MainLbl=Label(delframe,text="Enter User Id (to be deleted)").grid(row=1,column=2)
        delframe.pack(pady=10,padx=10)
        userLbl=Label(delframe,text="Username").grid(row=2,column=1)
        userTxt=Entry(delframe)

       #function to validate user id and delete  user id
        def delete():
            log('inside delete user function')
            userid=userTxt.get()
            log('user entered values: uid: ',userid)
            log('List of current Users:',UID.keys())
            if  userid in UID:
                log('user id is present in dictionary')
                log('connecting to DB to delete user')          
                del_stmt="delete from users where uid='"+userid+"' and UType='user';"
                log('QUERY TO BE EXECUTED:',del_stmt)
                mycur.execute(del_stmt)
                mycur.execute('commit;')
                log('User ID deleted from user table')
                del UID[userid]
                log('list of current user ids :',UID)
                messagebox.showinfo("User ID deleted!",userid+"  has been deleted succesfully. ",)
                del_win.destroy()
            else:
                reenter=Label(delframe,text=" User id does not exist. re enter correct id",fg='red',bg='white').grid(row=2,column=3)

##         Arranging display using grid   
        userTxt.grid(row=2,column=2)
        DelBt=Button(delframe,text="DELETE USER",command=delete).grid(row=5,column=1)
##        function to go back
        def back():
            del_win.destroy()

        BackBt=Button(delframe,text="GO BACK",command=back).grid(row=5,column=2)
        
        del_win.mainloop()
##end of del user function

##Function to change password
def change():
        Chg_win=Tk()
        Chg_win.title('CRS: Password Change')
        Chgframe=Frame(Chg_win)
        MainLbl=Label(Chgframe,text="Enter User Id (whose password needs to be changed)").grid(row=1,column=2)
        Chgframe.pack(pady=10,padx=10)
        userLbl=Label(Chgframe,text="Username").grid(row=2,column=1)
        userTxt=Entry(Chgframe)
        bullet="\u2022"     
        npwdLbl=Label(Chgframe,text="New Password").grid(row=3,column=1)
        npwdTxt=Entry(Chgframe)
        npwdTxt.config(show=bullet)
        cpwdLbl=Label(Chgframe,text="Confirm New Password").grid(row=4,column=1)
        cpwdTxt=Entry(Chgframe)
       #function to validate user id password 
        def check():
            userid=userTxt.get()
            newpwd=npwdTxt.get()
            cpwd=cpwdTxt.get()
            log('user entered values: uid: ',userid, 'pwd:',newpwd, '\nConfirm pwd:',cpwd)
            if  userid not in AUID and userid not in UID:
                log('user id Does not Exist in dictionary')
                reenter=Label(Chgframe,text=" User id  Does not Exist!! Enter valid ID",fg='red',bg='white').grid(row=2,column=3)
            elif newpwd!=cpwd:
                log('Passwords dont match')
                repwd=Label(Chgframe,text=" Passwords dont match!! Re enter password",fg='red',bg='white').grid(row=4,column=3)
            else:
                log('Changing Password for given user id')
                if userid in UID:
                    UID[userid]=newpwd
                    update_stmt="update users set pwd='"+newpwd+"' , log='password changed by admin' where uid='"+userid+"' and UType='user';"
                elif userid in AUID:
                    AUID[userid]=newpwd
                    update_stmt="update users set pwd='"+newpwd+"', log='password changed by admin' where uid='"+userid+"' and UType='admin';"
                log('connecting to DB to change password ')
                log('QUERY TO BE EXECUTED:',update_stmt)
                mycur.execute(update_stmt)
                mycur.execute('commit;')
                log('Password changed in user table')
                log('list of current ids :',AUID,'\n',UID)
                messagebox.showinfo("Password Changed!"," Your password has been changed succesfully. \npress OK to LOG IN and continue",)
                Chg_win.destroy()
            ##End of check function
##         Arranging display using grid   
        userTxt.grid(row=2,column=2)
        npwdTxt.grid(row=3,column=2)
        cpwdTxt.grid(row=4,column=2)
        SignBt=Button(Chgframe,text="Submit",command=check).grid(row=5,column=1)
        def back():
            Chg_win.destroy()

        BackBt=Button(Chgframe,text="GO BACK",command=back).grid(row=5,column=2)
        
        Chg_win.mainloop()

##        End of Change function

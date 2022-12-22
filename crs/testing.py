from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog,simpledialog

##frame=Frame(root)
class megha(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initialize_user_interface()
    def initialize_user_interface(self):
        self.parent.title("canvas test")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")
        self.dose_label=Label(self.parent,text="dose")
        self.dose_entry=Entry(self.parent)
        self.dose_label.grid(row=0,column=0)
        self.dose_entry.grid(row=0,column=1)
        self.dose2_lbl=Label(self.parent,text="date")
        self.dose2_entry=Entry(self.parent)
        self.dose2_lbl.grid(row=1,column=0)
        self.dose2_entry.grid(row=1,column=1)
##        locality=data1
##        state=data2
        self.butt=Button(self.parent,text="insert",command=self.insert_data).grid(row=2,column=1)
        self.butt1=Button(self.parent,text="exit",command=self.parent.quit).grid(row=0,column=3)
        self.tree=Treeview(self.parent,columns=("dose","dose2"))
        self.tree.heading("#0",text="sno")
        self.tree.heading("#1",text="dose")
        self.tree.heading("#2",text="dose2")
        self.tree.column("#1",stretch=YES)
        self.tree.column("#2",stretch=YES)
        self.tree.column("#0",stretch=YES)
        self.tree.grid(row=4,columnspan=4)
        self.treeview=self.tree
        self.i=0

    def  insert_data(self):
        self.treeview.insert("","end",text="item_"+str(self.i),values=(self.dose_entry.get()+"mg",self.dose2_entry.get()))
        self.i=self.i+1
##        self.treeview.insert("","end",text=str(self.i),values=(locality,state))
##        self.i=self.i+1
def main():    
    root=Tk()
    
##    frame=Frame(root)
    d=megha(root)
    root.mainloop()
if __name__=="__main__":
    
    main()

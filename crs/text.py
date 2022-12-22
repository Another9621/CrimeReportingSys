from tkinter import *
root=Tk()
def retrieve_input():
    inputValue=textbox.get("1.0","end-1c")
    updated=inputValue

textbox=Text(root, height=2, width=10)
textbox.insert(INSERT,"megha")
textbox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input()).pack()

mainloop()

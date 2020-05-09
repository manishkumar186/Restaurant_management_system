from tkinter.ttk import Treeview
from tkinter import *
from connectionfile import *
from tkinter.messagebox import *
from tkinter.font import *
class search:
    def __init__(self):
        self.window=Tk()
        self.window.config(bg="mint cream")
        self.window.geometry("608x292")
        self.window.resizable(FALSE,FALSE)

        self.font1 = Font(family="Times New Roman", size=15, weight="bold", slant="italic",)

        self.frame3 = Frame(self.window, width=605, height=60, bg="blue", bd=10, relief="ridge")
        self.frame3.place(x=0, y=0)

        self.lb1=Label(self.window,text="ENTER MENU",bg="blue",font=self.font1)
        self.textbox1=Entry(self.window,width=30,bd=5,relief="ridge")
        self.bt1=Button(self.window,text="SEARCH",bd=3,width=10,relief="ridge",command=self.search)
        self.bt2=Button(self.window,text="CLOSE",bd=3,width=10,relief="ridge",command=self.window.destroy)
        self.bt1.place(x=370,y=15)
        self.bt2.place(x=470,y=15)
        self.lb1.place(x=20,y=15)
        self.textbox1.place(x=170,y=15)
        self.t1 = Treeview(self.window, columns=("MENU NAME", "DESCRIPTION", "PRICE"))
        self.t1.heading("MENU NAME", text="MENU NAME")
        self.t1.heading("DESCRIPTION", text="DESCRIPTION")
        self.t1.heading("PRICE", text="PRICE")
        self.t1["show"] = "headings"
        self.t1.place(x=3,y=62)
        self.window.mainloop()
    def search(self):
        itenname=self.textbox1.get()
        if  itenname=="":
            showinfo("","ENTER MENU NAME")
        elif not(self.textbox1.get()).isalpha():
            showinfo("","PLEASE ENTER VALID MENU")
        else:
            conn = connectionfile.connect('')
            s="select * from hotel where menuname LIKE '"+itenname+"%'"
            cr=conn.cursor()
            cr.execute(s)
            result=cr.fetchall()
            i=0
            for row in self.t1.get_children():
                self.t1.delete(row)
            for row in result:
                self.t1.insert("", index=i, values=row)
                i = i + 1
#obj=search()
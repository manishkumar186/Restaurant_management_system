from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
from tkinter.ttk import Combobox

from connectionfile import *
class addemployee:
    def __init__(self):
        self.window=Tk()
        self.window.title("                                   ADD EMPLOYEE")
        #self.window.config(bg="mint cream")
        self.window.geometry("400x250")
        self.window.resizable(FALSE,FALSE)
        self.frame2 = Frame(self.window, width=400, height=250, bg="orange", bd=10, relief="ridge")
        self.frame2.place(x=0, y=0)

        self.lb1=Label(self.window,text="EMAIL",bg="orange")
        self.lb2 = Label(self.window, text="NAME",bg="orange")
        self.lb3 = Label(self.window, text="MOBILE NUMBER",bg="orange")
        self.lb4 = Label(self.window, text="PASSWORD",bg="orange")
        self.lb5 = Label(self.window, text="POSITION",bg="orange")
        self.textbox1=Entry(self.window,bd=5,relief="ridge")
        self.textbox2 = Entry(self.window,bd=5,relief="ridge")
        self.textbox3 = Entry(self.window,bd=5,relief="ridge")
        self.textbox4 = Entry(self.window,bd=5,relief="ridge")
        self.cb1=Combobox(self.window,values=("CASHIER","KITCHEN"),state="readonly")
        self.bt1=Button(self.window,text="ADD",bg="yellow",command=self.insert)
        self.bt2 = Button(self.window, text="CLOSE", bg="yellow", command=self.window.destroy)

        self.lb1.place(x=10,y=20)
        self.lb2.place(x=10,y=60)
        self.lb3.place(x=10,y=100)
        self.lb4.place(x=10,y=140)
        self.lb5.place(x=10,y=180)
        self.textbox1.place(x=120,y=20)
        self.textbox2.place(x=120,y=60)
        self.textbox3.place(x=120,y=100)
        self.textbox4.place(x=120,y=140)
        self.cb1.place(x=120,y=180)
        self.bt1.place(x=100,y=210)
        self.bt2.place(x=220, y=210)
        self.window.mainloop()


    def insert(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "" or self.textbox3.get() == ""or self.textbox4.get() == ""or self.cb1.get() == "":
            showinfo('', 'PLEASE FILL ALL DETAILS')
        elif str(self.textbox1.get()).count("@")!=1:
            showinfo("","INVALED EMAIL")
        elif not str(self.textbox2.get()).isalpha():
            showinfo("","PLEASE ENTER VALID NAME")
        elif not str(self.textbox3.get()).isdigit():
            showinfo("","PLEASE ENTER VALID MOBILE NUMBER")
        elif len(self.textbox3.get())!=10:
            showinfo("","PLEASE ENTER VALID MOBILE NUMBER")

        else:
            s = "insert into employee values('" + self.textbox1.get() + "','" + self.textbox2.get() + "','" + self.textbox3.get() + "','" + self.textbox4.get() + "','"+self.cb1.get()+"')"
            conn=connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "SUCCESSFULLY ADDED")


#obj=addemployee()
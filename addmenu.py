from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
from connectionfile import *


class addmenu:
    def __init__(self):

        self.window = Toplevel()
        self.window.geometry("400x350")
        self.window.resizable(FALSE,FALSE)

        self.frame1 = Frame(self.window, width=400, height=60, bg="red",bd=8,relief="ridge")
        self.frame2 = Frame(self.window, width=400, height=250, bg="orange",bd=10,relief="ridge")
        self.frame3 = Frame(self.window, width=400, height=40, bg="maroon",bd=10,relief="ridge")

        self.font = Font(family="Times New Roman", size=20, weight="bold", slant="italic", underline=1)
        self.font1= Font(family="Times New Roman", size=10, weight="bold", slant="italic", underline=1)

        self.lb4=Label(self.window,text="ADD MENU",font=self.font,bg="red")

        self.lb1 = Label(self.window, text="MENU NAME",bg="orange",font=self.font1)
        self.lb2 = Label(self.window, text="DESCRIPTION",bg="orange",font=self.font1)
        self.lb3 = Label(self.window, text="PRICE",bg="orange",font=self.font1)


        self.textbox1 = Entry(self.window,width=27,bd=5)
        self.textbox2 = Text(self.window,width=20,height=5,bd=5)
        self.textbox3 = Entry(self.window,width=27,bd=5)
        self.bt1 = Button(self.window,text="ADD",width=10,bg="pink",command=self.insert)

        self.bt2 = Button(self.window, text="close", width=10, bg="pink",command=self.window.destroy)


        self.frame1.place(x=0, y=0)
        self.frame2.place(x=0, y=61)
        self.frame3.place(x=0, y=310)

        self.lb4.place(x=100,y=10)
        self.lb1.place(x=10,y=80)
        self.lb2.place(x=10,y=130)
        self.lb3.place(x=10,y=230)
        self.bt1.place(x=80,y=270)
        self.bt2.place(x=210,y=270)

        self.textbox1.place(x=200,y=80)
        self.textbox2.place(x=200,y=130)
        self.textbox3.place(x=200,y=230)
        self.window.mainloop()

    def insert(self):
        if self.textbox1.get()=="" or self.textbox2.get(0.1,END)=="" or self.textbox3.get()=="":
            showinfo('','PLEASE FILL ALL DETAIL')
        elif not(self.textbox1.get()).isaplha():
            showinfo("","PLEASE ENTER VALID MENU")
        elif not(self.textbox3.get()).isnumeric():
            showinfo("", "PLEASE ENTER VALID PRICE")

        else:
            s="insert into hotel values(NULL,'"+self.textbox1.get()+"','"+self.textbox2.get(0.1,END)+"','"+self.textbox3.get()+"')"
            conn = connectionfile.connect('')
            cr=conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("","ORDER ADDED")

#obj=addmenu();
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from connectionfile import *
class manageemployee:
    def __init__(self):
        self.window=Tk()
        self.window.config(bg="mint cream")
        self.window.geometry("400x365")
        self.window.resizable(FALSE,FALSE)


        self.frame1 = Frame(self.window, width=400, height=60, bg="pink", bd=8, relief="ridge")
        self.frame2 = Frame(self.window, width=400, height=250, bg="orange", bd=10, relief="ridge")
        self.frame3 = Frame(self.window, width=400, height=50, bg="gold", bd=10, relief="ridge")

        self.frame1.place(x=0, y=0)
        self.frame2.place(x=0, y=61)
        self.frame3.place(x=0, y=310)


        self.lb1=Label(self.window,text="SELECT",bg="pink")
        self.lb2 = Label(self.window, text="NAME",bg="orange")
        self.lb3 = Label(self.window, text="MOBILE",bg="orange")
        self.lb4 = Label(self.window, text="PASSWORD",bg="orange")
        self.lb5 = Label(self.window, text="POSITION",bg="orange")

        self.cb1=Combobox(self.window,state="readonly")
        self.textbox1=Entry(self.window)
        self.textbox2 = Entry(self.window)
        self.textbox3 = Entry(self.window)
        self.textbox4 = Entry(self.window)

        self.bt1=Button(self.window,text="DETAIL",command=self.detail)
        self.bt2 = Button(self.window, text="DELETE",command=self.delete)
        self.bt3 = Button(self.window, text="EDIT",command=self.edit)
        self.bt4 = Button(self.window, text="CLOSE", command=self.window.destroy)

        self.lb1.place(x=10,y=20)
        self.lb2.place(x=10,y=70)
        self.lb3.place(x=10,y=110)
        self.lb4.place(x=10,y=150)
        self.lb5.place(x=10,y=190)

        self.cb1.place(x=80,y=20)
        self.textbox1.place(x=150,y=70)
        self.textbox2.place(x=150,y=110)
        self.textbox3.place(x=150,y=150)
        self.textbox4.place(x=150,y=190)

        self.bt1.place(x=250,y=20)
        self.bt2.place(x=80,y=320)
        self.bt3.place(x=200,y=320)
        self.bt4.place(x=300, y=320)

        l = []
        s = "select * from employee"
        conn = connectionfile.connect('')
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        for row in result:
            menuid = row[0]
            l.append(str(menuid))
        self.cb1["values"] = l
        self.window.mainloop()

    def detail(self):
        si = self.cb1.get()
        if si == "":
            showinfo('', 'SELECT ANY EMAIL')
        else:
            conn = connectionfile.connect('')
            s = "select * from employee where email='"+si+"'"
            cr = conn.cursor()
            n= cr.execute(s)
            row = cr.fetchone()
            self.textbox1.delete(0, END)
            self.textbox2.delete(0, END)
            self.textbox3.delete(0, END)
            self.textbox4.delete(0, END)
            if n>0:
                self.bt1["state"] = "normal"
                self.textbox1.insert(0, str(row[1]))
                self.textbox2.insert(0, str(row[2]))
                self.textbox3.insert(0, str(row[3]))
                self.textbox4.insert(0, str(row[4]))

    def delete(self):
        si = self.cb1.get()
        if si == "":
            showinfo('', 'select any employee')
        else:
            conn = connectionfile.connect('')
            s = "delete from employee where email='"+si+"'"
            cr = conn.cursor()
            n = cr.execute(s)
            conn.commit()
            self.textbox1.delete(0, END)
            self.textbox2.delete(0, END)
            self.textbox3.delete(0, END)
            self.textbox4.delete(0, END)
            self.cb1['values']=""
            l = []
            s = "select * from employee"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchall()
            for row in result:
                menuid = row[0]
                l.append(str(menuid))
            self.cb1["values"] = l
            self.cb1.current(0)
            showinfo('','DELETE SUCCESSFULLY')

    def edit(self):
        si = self.cb1.get()
        if si == "":
            showinfo('', 'SELECT ANY DETAIL')
        elif not str(self.textbox1.get()).isalpha():
            showinfo("","PLEASE ENTER VALID NAME")
        elif not str(self.textbox2.get()).isdigit():
            showinfo("","PLEASE ENTER VALID MOBILE NUMBER")
        elif len(self.textbox2.get())!=10:
            showinfo("","PLEASE ENTER VALID MOBILE NUMBER")
        else:
            conn = connectionfile.connect('')
            s = "update employee set name='" + self.textbox1.get() + "',mobile='" + self.textbox2.get() + "',password='"+ self.textbox3.get()+"',position='"+ self.textbox4.get()+"' where email='"+si+"'"
            cr = conn.cursor()
            n = cr.execute(s)
            conn.commit()
            showinfo('', 'UPDATE SUCCESSFULLY')
            self.textbox1.delete(0,END)
            self.textbox2.delete(0,END)
            self.textbox3.delete(0,END)
            self.textbox4.delete(0,END)





#obj=manageemployee()
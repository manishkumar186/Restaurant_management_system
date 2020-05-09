from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from connectionfile import *


class manageitems:
    def __init__(self):

        self.window=Toplevel()
        self.window.geometry("400x365")
        self.window.resizable(FALSE,FALSE)

        self.frame1 = Frame(self.window, width=400, height=60, bg="gold", bd=8, relief="ridge")
        self.frame2 = Frame(self.window, width=400, height=250, bg="pink", bd=10, relief="ridge")
        self.frame3 = Frame(self.window, width=400, height=50, bg="blue", bd=10, relief="ridge")

        self.frame1.place(x=0, y=0)
        self.frame2.place(x=0, y=61)
        self.frame3.place(x=0, y=310)



        self.cb1 = Combobox(self.window,state="readonly")

        self.lb4 = Label(self.window, text="SELECT",bg="gold")
        self.lb1 = Label(self.window, text="MENU NAME",bg="pink")
        self.lb2 = Label(self.window, text="DESCRIPTION",bg="pink")
        self.lb3 = Label(self.window, text="PRICE",bg="pink")

        self.textbox1 = Entry(self.window,bd=5,relief="ridge")
        self.textbox2 = Entry(self.window,bd=5,relief="ridge")
        self.textbox3 = Entry(self.window,bd=5,relief="ridge")

        self.lb1.place(x=50, y=80)
        self.lb2.place(x=50, y=130)
        self.lb3.place(x=50, y=180)
        self.lb4.place(x=50, y=20)

        self.textbox1.place(x=200, y=80)
        self.textbox2.place(x=200, y=130)
        self.textbox3.place(x=200, y=180)
        self.cb1.place(x=130, y=20)

        self.bt1=Button(self.window,text="DELETE",bg="white",command=self.delete)
        self.bt2 = Button(self.window, text="GET DETAIL",bg="white",command=self.detail)
        self.bt3 = Button(self.window, text="EDIT",bg="white",command=self.edit)
        self.bt4 = Button(self.window, text="CLOSE", bg="white",command=self.window.destroy)
        self.bt3.place(x=60,y=320)
        self.bt1.place(x=180,y=320)
        self.bt2.place(x=300,y=20)
        self.bt4.place(x=300, y=320)



        l = []
        s = "select * from hotel"
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
            showinfo('', 'select any menu')
        else:
            conn = connectionfile.connect('')
            s = "select * from hotel where order_number=" + si
            cr = conn.cursor()
            n = cr.execute(s)
            row = cr.fetchone()
            self.textbox1.delete(0, END)
            self.textbox2.delete(0, END)
            self.textbox3.delete(0, END)
            if n > 0:
                self.bt2["state"] = "normal"
                self.textbox1.insert(0, str(row[1]))
                self.textbox2.insert(0, str(row[2]))
                self.textbox3.insert(0, str(row[3]))

    def delete(self):
        si = self.cb1.get()
        if si == "":
            showinfo('', 'select any menu')
        else:
            conn = connectionfile.connect('')
            s = "delete from hotel where order_number=" + si
            cr = conn.cursor()
            n = cr.execute(s)
            conn.commit()
            self.textbox1.delete(0, END)
            self.textbox2.delete(0, END)
            self.textbox3.delete(0, END)
            self.cb1['values']=""
            l = []
            s = "select * from hotel"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchall()
            for row in result:
                menuid = row[0]
                l.append(str(menuid))
            self.cb1["values"] = l
            self.cb1.current(0)
            showinfo('', 'item deleted succwssfully')

    def edit(self):
        si = self.cb1.get()
        if si == "":
            showinfo('', 'SELECT ANY MENU')
        elif not (self.textbox1.get()).isalpha():
            showinfo("", "PLEASE ENTER VALID MENU")
        elif not(self.textbox3.get()).isnumeric():
            showinfo("", "PLEASE ENTER VALID PRICE")
        else:
            conn = connectionfile.connect('')
            s = "update hotel set menuname='" + self.textbox1.get() + "',description='" + self.textbox2.get() + "',price=" + self.textbox3.get() + " where order_number=" + si + ""
            cr = conn.cursor()
            n = cr.execute(s)
            conn.commit()
            showinfo('', 'item updated successfully')


#obj=manageitems()

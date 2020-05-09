from mainmenu import *
from tkinter.font import Font
from tkinter import *
class employeelogin:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("900x350")
        self.window.resizable(FALSE, FALSE)
        #self.window.config(bg="mint cream")
        #self.window.title("                       EMPLOYEE LOGIN")

        self.frame1=Frame(self.window, width=900, height=75,bg="red",bd=10,relief="ridge")
        self.frame2=Frame(self.window, width=900, height=170, bg="pink",bd=10,relief="ridge")
        self.frame3=Frame(self.window, width=900, height=50, bg="maroon",bd=10,relief="ridge")
        self.frame4 = Frame(self.window, width=900, height=70, bg="blue",bd=10,relief="ridge")


        self.font = Font(family="Times New Roman", size=30, weight="bold", slant="italic", underline=1)
        self.font1 = Font(family="Times New Roman", size=25, weight="bold", slant="italic", underline=1)
        self.font2 = Font(family="Times New Roman", size=10, weight="bold", slant="italic", underline=1)



        self.fontlabel=Label(self.window, text="RESTAURANT MANAGEMENT SYSTEM",bg="red",font=self.font);
        self.fontlabe2 = Label(self.window, text="LOGIN PAGE", bg="blue", font=self.font1);
        self.lb1=Label(self.window,text="POSITION",font=self.font2,bg="pink")
        self.lb2 = Label(self.window, text="EMAIL",font=self.font2,bg="pink")
        self.lb3 = Label(self.window, text="PASSWORD",font=self.font2,bg="pink")
        self.cb1=Combobox(self.window,values=("CASHIER","KITCHEN"),state="readonly")
        self.textbox1=Entry(self.window,width=23,bd=2)
        self.textbox2 = Entry(self.window,width=23,bd=2)
        self.bt1=Button(self.window,text="LOGIN",bg="gold",command=self.login)

        self.frame1.place(x=0, y=0)
        self.frame4.place(x=0, y=75)
        self.frame2.place(x=0, y=140)
        self.frame3.place(x=0,y=300)

        self.lb1.place(x=250,y=150)
        self.cb1.place(x=370, y=150)

        self.fontlabel.place(x=70,y=8);
        self.fontlabe2.place(x=350, y=85);

        self.lb2.place(x=250,y=190)
        self.textbox1.place(x=370, y=190)

        self.lb3.place(x=250,y=230)
        self.textbox2.place(x=370,y=230)

        self.bt1.place(x=400,y=260)
        self.window.mainloop()
    def login(self):
        conn = connectionfile.connect('')
        s="select * from employee where email='"+self.textbox1.get()+"'and password='"+self.textbox2.get()+"'and position='"+self.cb1.get()+"'"
        cr = conn.cursor()
        n=cr.execute(s)
        p=self.cb1.get()
        if n>0:

            showinfo("","LOGIN SUCCESSFULLY")
            self.window .destroy()
            if str(p)=="CASHIER":
                mainmenu()
                 #addmenu()
            elif str(p) == "KITCHEN":
                kitchenscreen()
                self.window.mainloop()

        else:
            showinfo("", "login fail")
obj=employeelogin()



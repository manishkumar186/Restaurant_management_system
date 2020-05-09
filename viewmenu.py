from tkinter import *
from tkinter.ttk import Treeview
from connectionfile import *
class viewmenu:
    def __init__(self):
        self.window=Tk()
        self.window.config(bg="maroon")
        self.window.geometry("900x470")
        self.window.resizable(FALSE,FALSE)

        self.t1 = Treeview(self.window,height=20,columns=("MENU ID","MENU NAME", "DESCRIPTION", "PRICE"))
        self.t1.heading("MENU ID", text="MENU ID")
        self.t1.heading("MENU NAME", text="MENU NAME")
        self.t1.heading("DESCRIPTION", text="DESCRIPTION")
        self.t1.heading("PRICE", text="PRICE")
        self.t1["show"] = "headings"

        self.bt1=Button(self.window,text="CLOSE",bg="pink",bd=3,relief="ridge",command=self.window.destroy)
        self.bt1.place(x=370,y=435)

        s ="select * from hotel"
        conn = connectionfile.connect('')
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1
        self.t1.pack()
        self.window.mainloop()
#obj=viewmenu()
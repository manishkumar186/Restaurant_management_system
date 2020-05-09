from tkinter import *
from tkinter.ttk import *
from connectionfile import *
class viewemployee:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("1000x300")
        self.window.resizable(FALSE,FALSE)
        self.t1 = Treeview(self.window, columns=("EMAIL", "NAME", "MOBILE","PASSWORD","POSITION"))
        self.t1.heading("EMAIL", text="EMAIL")
        self.t1.heading("NAME", text="NAME")
        self.t1.heading("MOBILE", text="MOBILE")
        self.t1.heading("PASSWORD", text="PASSWORD")
        self.t1.heading("POSITION", text="POSITION")
        self.t1["show"] = "headings"
        self.bt1=Button(self.window,text="CLOSE",command=self.window.destroy);
        self.bt1.place(x=350,y=250)
        s = "select * from employee"
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
#obj=viewemployee()



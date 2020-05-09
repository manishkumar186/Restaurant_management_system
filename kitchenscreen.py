from tkinter import *
from tkinter.ttk import *
from pymysql import *
from tkinter.messagebox import *
from connectionfile import *
from kitchendetail import *
class kitchenscreen:
    def __init__(self):
        self.window=Tk()
        self.window.config(bg="mint cream")
        self.window.geometry("1200x300")
        self.window.resizable(FALSE,FALSE)
        self.window.title('kitchen main screen')
        self.treeview=Treeview(self.window,columns=("BILL ID","BILL DATE","TYPE OF BILL","TOTAL BILL","TAX","STATUS"))
        self.treeview.heading("BILL ID",text="BILL ID")
        self.treeview.heading("BILL DATE", text="BILL DATE")
        self.treeview.heading("TYPE OF BILL", text="TYPE OF BILL")
        self.treeview.heading("TOTAL BILL", text="TOTAL BILL")
        self.treeview.heading("TAX", text="TAX")
        self.treeview.heading("STATUS", text="STATUS")
        self.treeview["show"] = "headings"
        conn = connectionfile.connect('')
        s="select * from bill where status='pending'"
        cr=conn.cursor()
        cr.execute(s)
        result=cr.fetchall()
        i=0
        for row in result:
            list=[row[0],row[1],row[3],row[5],row[6],row[10]]

            self.treeview.insert("",index=i,values=list)
            i=i+1
        self.treeview.grid(row=1,column=0,columnspan=1,rowspan=1)
        self.bt=Button(self.window,text="GET DETAIL",bg="pink",command=self.getdetail)
        self.bt.place(x=300,y=240)

        self.bt1 = Button(self.window, text="CLOSE",bg="pink", command=self.window.destroy)
        self.bt1.place(x=600,y=240)

        self.window.mainloop()
    def getdetail(self):
        si=0
        si=self.treeview.focus()
        d=self.treeview.item(si)
        lst=d['values']
        if str(lst)=='':
            showinfo('','SELECT ANY BILL TYPE')
        else:
            billid = lst[0]
            self.window.destroy()
            kitchendetail(billid)


#obj=kitchenscreen()




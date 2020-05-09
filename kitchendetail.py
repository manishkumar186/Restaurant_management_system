from tkinter import *
from tkinter.messagebox import *
from tkinter.font import *
from tkinter.ttk import Treeview

from connectionfile import *
class kitchendetail:
    def __init__(self,billid):
        self.window = Tk()
        self.window.title('kitchen detail screen')
        #self.window.config(bg="mint cream")
        self.window.geometry("1200x470")
        self.frame2 = Frame(self.window, width=1200, height=180, bg="orange", bd=10, relief="ridge")
        self.frame3 = Frame(self.window, width=1200, height=60, bg="maroon", bd=10, relief="ridge")

        self.frame2.place(x=0, y=0)
        self.frame3.place(x=0, y=408)

        self.bid = billid
        conn = connectionfile.connect('')
        s = "select * from bill where billid='" + str(self.bid) + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        billlist=[]
        for row in result:
            billlist=row
        #print(str(billlist))
        self.lb1=Label(self.window,bg="orange",text="BILL ID :"+str(billlist[0]))
        self.lb2 = Label(self.window,bg="orange", text="BILL DATE :" + str(billlist[1]))
        self.lb3 = Label(self.window,bg="orange", text="MOBILE :" + str(billlist[2]))
        self.lb4 = Label(self.window, bg="orange",text="TYPE OF BILL :" + str(billlist[3]))
        self.lb5 = Label(self.window, bg="orange",text="ADDRESS :" + str(billlist[4]))
        self.lb6 = Label(self.window,bg="orange", text="TOTAL BILL :" + str(billlist[5]))
        self.lb7 = Label(self.window,bg="orange", text="TAX :" + str(billlist[6]))
        self.lb8 = Label(self.window,bg="orange", text="MODE OF PAYMENT  :" + str(billlist[7]))
        self.lb9 = Label(self.window, bg="orange",text="CASH COLLECTED :" + str(billlist[8]))
        self.lb10 = Label(self.window, bg="orange",text="CASH RETURNED :" + str(billlist[9]))
        self.lb11 = Label(self.window, bg="orange",text="STATUS :" + str(billlist[10]))
        self.lb1.place(x=100,y=20)
        self.lb2.place(x=100,y=40)
        self.lb3.place(x=100,y=60)
        self.lb4.place(x=100,y=80)
        self.lb5.place(x=100,y=100)
        self.lb6.place(x=300,y=120)
        self.lb7.place(x=400,y=20)
        self.lb8.place(x=400,y=40)
        self.lb9.place(x=400,y=60)
        self.lb10.place(x=400,y=80)
        self.lb11.place(x=400,y=100)

        self.treeview=Treeview(self.window,columns=("BILL DETAIL ID","MENU ID","MENU NAME","PRICE","QUANTITY","TOTAL PRICE"))
        self.treeview.heading("BILL DETAIL ID",text="BILL DETAIL ID")
        self.treeview.heading("MENU NAME", text="MENU NAME")
        self.treeview.heading("MENU ID", text="MENU ID")
        self.treeview.heading("PRICE", text="PRICE")
        self.treeview.heading("QUANTITY", text="QUANTITY")
        self.treeview.heading("TOTAL PRICE", text="TOTAL PRICE")
        self.treeview["show"] = "headings"
        s="select * from billdetail where billid='"+str(self.bid)+"'"
        cr=conn.cursor()
        cr.execute(s)
        result=cr.fetchall()
        i=0
        for row in result:
            s = "select * from hotel where order_number='" + str(row[1]) + "'"
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchone()
            list = [row[0], row[1],str(result[1]), row[2], row[3], row[4]]

            self.treeview.insert("",index=i,values=list)
            i=i+1
        self.treeview.place(x=0,y=180)
        self.bt=Button(self.window,text="DONE",bg="pink",command=self.done)
        #self.bt1 = Button(self.window, text="CLOSE",bg="pink", command=self.window.destroy)
        self.bt.place(x=500,y=425)
        #self.bt1.place(x=600, y=425)
        self.window.mainloop()
    def done(self):
        conn = connectionfile.connect('')
        s = "update bill set status='done' where billid='" + str(self.bid) + "'"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo('','ORDER DONE SUCESSFULLY')
        self.window.destroy()
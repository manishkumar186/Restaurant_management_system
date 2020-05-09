from tkinter import *
from tkinter.ttk import Treeview
from tkcalendar import *
from reportlab.lib.pagesizes import A5,A4
from reportlab.pdfgen import canvas
from connectionfile import *
import subprocess
import random
from tkinter.messagebox import *
class showtotalbill:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("1200x355")
        self.window.resizable(FALSE,FALSE)

        self.frame1 = Frame(self.window, width=1200, height=60, bg="red", bd=8, relief="ridge")
        self.frame2 = Frame(self.window, width=1200, height=70, bg="orange", bd=10, relief="ridge")


        self.frame1.place(x=0, y=0)
        self.frame2.place(x=0, y=280)



        self.lb1=Label(self.window,text="DATE",bg="red")
        self.lb2 = Label(self.window, text="TOTAL SALE",bg="orange")
        self.bt1=Button(self.window,text="SELECT DATE",command=self.get)
        self.lb1.place(x=200,y=15)
        self.lb2.place(x=100,y=300)
        self.bt1.place(x=400,y=15)
        self.textbox1=DateEntry(self.window)
        self.textbox1.place(x=250,y=15)
        self.t1 = Treeview(self.window, columns=("BILLID", "MOBILE","TYPEOFBILL","TOTALBILL","TAX","MADEOFPAYMENT"))
        self.t1.heading("BILLID", text="BILLID")
        self.t1.heading("MOBILE", text="MOBILE")
        self.t1.heading("TYPEOFBILL", text="TYPEOFBILL")
        self.t1.heading("TOTALBILL", text="TOTALBILL")
        self.t1.heading("TAX", text="TAX")
        self.t1.heading("MADEOFPAYMENT", text="MADEOFPAYMENT")
        self.t1["show"] = "headings"
        self.t1.place(x=0,y=62)
        self.window.config(bg="mint cream")
        self.bt=Button(self.window,text="GENERATE PDF",command=self.pdf)
        self.bt.place(x=400,y=300)
        self.window.mainloop()

    def get(self):

        conn = connectionfile.connect('')
        s="select billid,mobile,typeofbill,totalbill,tax,madeofpayment from bill where status='done' and billdate='"+str(self.textbox1.get_date())+"'"
        cr = conn.cursor()
        n = cr.execute(s)
        result=cr.fetchall()
        i=0
        sum=0
        for row in result:
            self.t1.insert("",index=i,values=row)
            i=i+1

        for row in result:
            sum = sum + row[3]
        self.lb3 = Label(self.window, text=sum)
        self.lb3.grid(row=8,column=0)


    def pdf(self):

        name = str(random.randint(0, 100))
        name_pdf = str("pdfbills//a" + str(name) + ".pdf")
        my_canv = canvas.Canvas(name_pdf, pagesize=A5)
        my_canv.setFont('Helvetica', 14)
        my_canv.setLineWidth(.2)

        y = 580
        my_canv.drawString(160, y, 'Sales On '+str(self.textbox1.get_date()))
        my_canv.line(10, y - 3, 600, y - 3)

        my_canv.setFont('Helvetica', 10)
        my_canv.drawString(30, y - 12, "billid")
        my_canv.drawString(130, y - 12, "mobile")
        my_canv.drawString(230, y - 12, "type of bill")
        my_canv.drawString(330, y - 12, "total bill")
        my_canv.drawString(430, y - 12, "tax")
        my_canv.drawString(530, y - 12, "mode of payment")
        y = y - 12
        my_canv.line(10, y - 3, 600, y - 3)
        my_canv.setFont('Helvetica', 8)
        y = y - 3
        s = []
        conn = connectionfile.connect('')
        q = "select billid,mobile,typeofbill,totalbill,tax,madeofpayment from bill where status='done' and billdate='" + str(
            self.textbox1.get_date()) + "'"
        cr = conn.cursor()
        n = cr.execute(q)
        result = cr.fetchall()
        i = 0
        sum = 0
        for row in result:
            s.append(row)
            i = i + 1
        #print(s)
        for row in result:
            sum = sum + row[3]

        for i in range(0, len(s)):
            my_canv.drawString(30, y - 12, str(s[i][0]))
            my_canv.drawString(130, y - 12, str(s[i][1]))
            my_canv.drawString(230, y - 12, str(s[i][2]))
            my_canv.drawString(330, y - 12, str(s[i][3]))
            my_canv.drawString(430, y - 12, str(s[i][4]))
            my_canv.drawString(530, y - 12, str(s[i][5]))
            y = y - 12
        my_canv.line(10, y - 3, 500, y - 3)
        y = y - 3
        gst = ((float)(sum) * 5) / 100
        withoutgst=0.0
        withoutgst=sum-gst
        my_canv.drawString(230, y - 12, "Total")
        my_canv.drawString(230, y - 24, "GST")
        my_canv.drawString(230, y - 36, "Payable")
        my_canv.drawString(330, y - 12, str(withoutgst))


        my_canv.drawString(330, y - 24, "5%")
        my_canv.drawString(330, y - 36, str(sum))
        my_canv.save()
        subprocess.Popen([name_pdf], shell=True)
        showinfo('','PDF GENERATED SUCCESSFULLY')
        self.window.destroy();

#obj=showtotalbill()


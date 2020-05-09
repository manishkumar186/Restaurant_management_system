from addmenu import *
from viewmenu import *
from manageitems import *
from search import *
from cart import *
from kitchenscreen import *
from addemployee import *
from viewemployee import *
from manageemployee import *
from showtotalbill import *
from PIL import ImageTk,Image
class mainmenu:
    def fire1(self):
        obj1=addmenu()
    def fire2(self):
        obj2=viewmenu()
    def fire3(self):
        obj3=manageitems()
    def fire4(self):
        obj4=search()
    def fire5(self):
        obj5=cart()
    def fire6(self):
        obj6 = kitchenscreen()
    def fire7(self):
        obj7=addemployee()
    def fire8(self):
        obj8=viewemployee()
    def fire9(self):
        obj9=manageemployee()
    def fire10(self):
        obj10=showtotalbill()
    def __init__(self):
        self.window = Tk()
        self.window.geometry("305x173")
        self.window.resizable(FALSE,FALSE)
        self.window.config(bg="red")
        self.my_image=ImageTk.PhotoImage(Image.open("image.jpeg"))
        self.my_label=Label(image=self.my_image)
        self.my_label.place(x=0,y=0)
        self.mymenu = Menu(self.window)
        self.window.config(menu=self.mymenu)
        self.submenu1 = Menu(self.mymenu, tearoff=False)
        self.submenu2 = Menu(self.mymenu, tearoff=False)


        self.mymenu.add_cascade(label="MAIN MENU", menu=self.submenu1)
        self.mymenu.add_cascade(label="EMPLOYEE MENU", menu=self.submenu2)


        self.submenu1.add_command(label="ADD MENU", command=self.fire1)
        self.submenu1.add_command(label="VIEW MENU", command=self.fire2)
        self.submenu1.add_command(label="MANAGE ITEM", command=self.fire3)
        self.submenu1.add_command(label="SEARCH", command=self.fire4)
        self.submenu1.add_command(label="ADD TO CART", command=self.fire5)
        self.submenu1.add_command(label="KITCHEN SCREEN", command=self.fire6)

        self.submenu2.add_command(label="ADD EMPLOYEE", command=self.fire7)
        self.submenu2.add_command(label="VIEW EMPLOYEE", command=self.fire8)
        self.submenu2.add_command(label="MANAGE EMPLOYEE", command=self.fire9)
        self.submenu2.add_command(label="SHOW TOTAL BILL", command=self.fire10)
        self.window.mainloop()
#obj=mainmenu();



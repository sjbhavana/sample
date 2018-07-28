import fruitshop
import tkinter
from tkinter import messagebox
from tkinter import *
root=Tk()
root.title("RELIENCE FRESH SUPER MARKET")


e=list()
def done():
    def done1():
        a1=StringVar()
        a2=IntVar()
        def done2():
            name=a1.get()
            name=fruitshop.fruit(a1.get(),a2.get())
            messagebox.showinfo("Employee Added","succesfully added")
            fruitshop.fruit.e.append(a1.get()) 
        l1=Label(root1,text="Enter employee name:")
        l1.pack()
        e1=Entry(root1,textvariable=a1)
        e1.pack()
        l2=Label(root1,text="Enter employee salary:")
        l2.pack()
        e2=Entry(root1,textvariable=a2)
        e2.pack()
        b1=Button(root1,text="Register",command=done2)
        b1.pack()
         
    def sell():
        name2=a3.get()
        name2=fruitshop.fruit(name2)
        if(a3.get() in fruitshop.fruit.e):
            if(var2.get()=="mango"):
                if(fruitshop.fruit.mango<a4.get()):
                    messagebox.showerror("no stock","mangoes out of stock!!")
                if(fruitshop.fruit.mango>=a4.get()):
                    fruitshop.fruit.sell(name2,"mango",a4.get())
                    messagebox.showinfo("sell manoges", "successfuly sold mangoes!")
            if(var2.get()=="kiwi"):
                if(fruitshop.fruit.kiwi<a4.get()):
                    messagebox.showerror("no stock","kiwi fruits out of stock!!")
                if(fruitshop.fruit.mango<=a4.get()):
                    fruitshop.fruit.sell(name2,"kiwi",a4.get())
                    messagebox.showinfo("sell kiwi!", "successfuly sold kiwi!") 
        else:
            messagebox.showerror("Authentication error","Employee unregistered!!")
             
    def buy():
        name3=a5.get()
        name3=fruitshop.fruit(name3)
        if (a5.get() in fruitshop.fruit.e):
            if(var3.get()=="mango"):
                fruitshop.fruit.buy(name3,"mango",a6.get())
            if(var3.get()=="kiwi"):
                fruitshop.fruit.sell(name3,"kiwi",a6.get())
            messagebox.showinfo("buy sucesss!","Fruits succesfully bought!!")

        else:
            messagebox.showerror("Authentication error","Employee unregistered")
    if(var.get()=="Add Employee"):
        root1=Toplevel(root)
        root.title("ADITYA BIRLA GROUP")
        done1()
            
    if(var.get()=="Sell fruit"):
        root2=Toplevel(root)
        root2.title("Sell Fruit")
        a3=StringVar()
        a4=IntVar()
        var2=StringVar()
        var2.set("fruit")
        l3=Label(root2,text="Enter employee name:")
        l3.pack()
        e3=Entry(root2,textvariable=a3)
        e3.pack()
        l4=Label(root2,text="                    ")
        l4.pack()
        l5=Label(root2,text="select fruit")
        l5.pack()
        o1=OptionMenu(root2,var2,"mango","kiwi")
        o1.pack()
        l6=Label(root2,text="enter weight")
        l6.pack()
        e4=Entry(root2,textvariable=a4)
        e4.pack()
        b2=Button(root2,text="Sell",command=sell)
        b2.pack()

    if(var.get()=="Buy fruit"):
        root3=Toplevel(root)
        root3.title("Buy Fruit")
        a5=StringVar()
        a6=IntVar()
        var3=StringVar()
        var3.set("fruit")
        l7=Label(root3,text="Enter employee name:")
        l7.pack()
        e5=Entry(root3,textvariable=a5)
        e5.pack()
        l8=Label(root3,text="                    ")
        l8.pack()
        l9=Label(root3,text="select fruit")
        l9.pack()
        o2=OptionMenu(root3,var3,"mango","kiwi")
        o2.pack()
        l10=Label(root3,text="enter weight")
        l10.pack()
        e6=Entry(root3,textvariable=a6)
        e6.pack()
        b3=Button(root3,text="Buy",command=buy)
        b3.pack()

    if(var.get()=="See stock"):
            messagebox.showinfo("current stock","no of mangoes="+str(fruitshop.fruit.mango)+"\nno of kiwi fruits="+str(fruitshop.fruit.kiwi))

var=StringVar()
var.set("select")
        
o=OptionMenu(root,var,"Add Employee","Sell fruit","Buy fruit","See stock")
o.pack()

b=Button(root,text="Next",command=done)
b.pack()

root.mainloop()





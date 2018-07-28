import parking
import tkinter
from tkinter import messagebox
from tkinter import *
root=Tk()
root.title("THE ORION PARKING LOT")

def done():
    def done1():
        a1=StringVar()
        a2=IntVar()
        def done2():
            name=a1.get()
            name=parking.park(a1.get(),a2.get())
            messagebox.showinfo("Employee Added","succesfully added")
            parking.park.e.append(a1.get())
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
            
    def count():
        name2=a3.get()
        name2=parking.park(name2)
        parking.park.n.append(a4.get())
        if (a3.get() in parking.park.e):
            if(var2.get()=="two"):
                if(a4.get() in parking.park.n):
                    parking.park.count(name2,"two",a4.get())
                    messagebox.showinfo("park vehicle", "successfuly parked!!")
            if(var2.get()=="four"):
                if(a4.get() in parking.park.n):
                    parking.park.count(name2,"four",a4.get())
                    messagebox.showinfo("park vehicle", "successfuly parked!") 
        else:
            messagebox.showerror("Authentication Error","Employee Unregistered")
    def bill():
        name3=a5.get()
        name3=parking.park(name3)
        if (a5.get() in parking.park.e):
            if(var3.get()=="two"):
                if(parking.park.two==0):
                    messagebox.showerror("Error","No vehicles parked yet!!")
                else:
                    if(a9.get() in parking.park.n):
                        parking.park.bill(name3,"two",a9.get(),a6.get())
                        messagebox.showinfo("Billing","Billing done succesfully!!\n total="+str(parking.park.twocost))
                    else:
                        messagebox.showinfo("Error","vehicle is not in parking lot")
            if(var3.get()=="four"):
                if(parking.park.two==0):
                    messagebox.showerror("Error","No vehicles parked yet!!")
                else:
                    if(a9.get() in parking.park.n ):
                        parking.park.bill(name3,"four",a9.get(),a6.get())
                        messagebox.showinfo("Billing","Billing done succesfully!!\n total="+str(parking.park.fourcost))
                    else:
                        messagebox.showerror("Error","Vehicle is not in parking lot")
        else:
            messagebox.showerror("Autentication Error","Employee Unregistered")
           
    if(var.get()=="Add Employee"):
        root1=Toplevel(root)
        root.title("ADITYA BIRLA GROUP")
        done1()
            
    if(var.get()=="Park vehicle"):
        root2=Toplevel(root)
        root2.title("Parking vehicle")
        a3=StringVar()
        a4=StringVar()
        var2=StringVar()
        var2.set("select")
        l3=Label(root2,text="Enter employee name:")
        l3.pack()
        e3=Entry(root2,textvariable=a3)
        e3.pack()
        l4=Label(root2,text="                    ")
        l4.pack()
        l5=Label(root2,text="vehicle type")
        l5.pack()
        o1=OptionMenu(root2,var2,"two","four")
        o1.pack()
        l6=Label(root2,text="vehicles number")
        l6.pack()
        e4=Entry(root2,textvariable=a4)
        e4.pack()
        b2=Button(root2,text="park",command=count)
        b2.pack()

    if(var.get()=="Billing"):
        root3=Toplevel(root)
        root3.title("Bill")
        a5=StringVar()
        i=IntVar()
        a6=StringVar()
        a9=StringVar()
        var3=StringVar()
        var3.set("select")
        var7=StringVar()
        var7.set("vehicle number")
        l7=Label(root3,text="Enter employee name:")
        l7.pack()
        e5=Entry(root3,textvariable=a5)
        e5.pack()
        l8=Label(root3,text="                    ")
        l8.pack()
        l9=Label(root3,text="vehicle")
        l9.pack()
        o2=OptionMenu(root3,var3,"two","four")
        o2.pack()
        l15=Label(root3,text="vehicle number")
        l15.pack()
        e17=Entry(root3,textvaribale=a9)
        e17.pack()
        l10=Label(root3,text="Enter time in hours")
        l10.pack()
        e6=Entry(root3,textvariable=a6)
        e6.pack()
        b3=Button(root3,text="Bill",command=bill)
        b3.pack()

    if(var.get()=="See status"):
            messagebox.showinfo("Parking lot status","no of two wheelers="+str(parking.park.two)+"\nno of four wheelers="+str(parking.park.four))

    if(var.get()=="Daily Turnover"):
        messagebox.showinfo("Profit window","profit by two wheelers= $"+str(parking.park.twobill)+"\nprofit by four wheelers= $"+str(parking.park.fourbill)+"\n-----------------------------------"+"\nTotal profit= $"+str(parking.park.twobill+parking.park.fourbill) )
        
var=StringVar()
var.set("select")
        
o=OptionMenu(root,var,"Add Employee","Park vehicle","Billing","See status","Daily Turnover")
o.pack()

b=Button(root,text="Next",command=done)
b.pack()

root.mainloop()





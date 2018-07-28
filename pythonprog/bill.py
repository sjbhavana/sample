units=int(input("enter the number of units utilized:"))
amt=0
if(units<=100):
    amt=units*60
elif(units>100 and units<=300):
    amt=6000+(units-100)*70
elif(units>300):
    amt=6000+14000+(units-300)*80
print("total amount for consumption of",units,"units is",amt,"cents")

#name of shape to be determined by the number of sides.

n=int(input("enter the number of sides:"))
if n>=3 and n<=10:
    if n==3:
        print("it is a trinagle")
    elif n==4:
        print("it is a quadrilateral")
    elif n==5:
        print("it is a pentagon")
    elif n==6:
        print("it is a hexagon")
    elif n==7:
        print("it is a heptagon")
    elif n==8:
        print("it is a octagon")
    elif n==9:
        print("it is a nanaogon")
    else:
        print("it is a decagon")
else:
     print(" ERROR!!! entered number of sides is out of range!!!!")

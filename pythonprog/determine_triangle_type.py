#determine the type of the triangle
print("enter the sides of the triangle")
a=float(input("enter the side one:"))
b=float(input("enter the side two:"))
c=float(input("enter the side three:"))
if a==b and b==c and a==c:
    print("it is a eqilateral triangle!!")
elif a==b or b==c or a==c:
    print("it is a isoceles triangle")
else:
    print("it is a scalene triangle")
      

#to find the circumference and volume of the circle.

import math
r=float(input("enter the radius of the circle in m:  "))
c=2*math.pi*r
print("circumference of the circle is:",format(c,".2f"),"m")
a=math.pi*r**2
print("area of circle is:",format(a,".2f"),"sqm")
v=(4/3)*math.pi*r**3
print("volume is:",format(v,".2f"),"cubm")

# 3 integer sort

print("enter the elements to the list:")
a=int(input("enter the first element:"))
b=int(input("enter the second element:"))
c=int(input("enter the third element:"))
print("list to be sorted is: [" ,a,"," , b,",", c, "]")
x=min(a,b,c)
y=max(a,b,c)
z=(a+b+c)-x-y
print("sorted list will is: [" ,x,",", z ,"'",y ,"]")

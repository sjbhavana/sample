m=int(input("enter the first number:"))
n=int(input("enter the other number:"))
gcd=min(m,n)
while n%gcd!=0 or m%gcd!=0:
    gcd=gcd-1
print("the gcd of", m,n,"is",gcd)

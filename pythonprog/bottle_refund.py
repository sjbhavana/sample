#bottle_refund

#l=float(input("enter the quantity of water bottle in liters"))
#if l<=1:
 #   n=int(input("enter the number of 1 liter bottles:"))
  #  refund=n*0.10
   # print("refund for", n ," 1 liter bottles=  $",format(refund,".2f"))
#else:
 #   num=int(input("enter the number of bottles with quantity greater than one liter:"))
  #  refund2=num*0.25
   # print("refund for", num," bottles= $",format(refund2,".2f"))

totalref=0
refund=0
n=int(input("enter the total number of bottles"))
while n>0:
    quant=float(input("enter the bottle quantity"))
    num=int(input("enter the number of bottles:"))
    if quant<1.0:
        refund=num*0.1
    else:
        refund=num*0.25
    n-=num
    totalref=totalref+refund
print("total refund amount=$",format(totalref,".2f"))

# program to calculate parity using even parityfor group of 8 bits enered by user
count=0
p=input("enter the 8 bit binary string:")
leng=len(p)
if(leng==8):
    print("please wait while your data is being processed!!!")
    for i in p:
        if(i=="1"):
            count+=1
    if (count%2)==0:
        print("the parity bit should be set to 0.")
        print("the string will be: 0",p)
    else:
        print("the parity bit should be set to 1.")
        print("the string will be: 1",p)

else:
    print("enter the valid string!!!")
    exit()
    





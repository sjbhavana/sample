inp=input("enter the stream of characters and numbers")
alpa=0
num=0
for i in inp:
    if i.isdigit():
        num+=1
    elif i.isalpha():
        alpa+=1
    else:
        pass
print("number of iteger=",num)
print("number of alphabets=",alpa)

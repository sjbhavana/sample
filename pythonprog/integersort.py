def bubblesort(l):
    for item in range(len(l)-1,0,-1):
        for i in range(item):
            if l[i]>l[i+1]:
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp
    return l

l=list()
res=list()
n=int(input("enter the number of elements to be sorted:"))

for i in range(n):
    value=input("enter the element")
    l.append(value)
print("list to be sorted will be:")
for i in range(len(l)):
    print(l[i],end=" ")
    
print("\nsorted list will be:")

res=bubblesort(l)

for j in range(len(res)):
    print(res[j],end=" ")

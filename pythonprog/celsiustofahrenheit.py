#celsius to farenhieh coversion table
c=list(range(0,101,10))
f=list()
print("celsius list: " ,c )
for i in range(len(c)):
    far=9/5*c[i]+32
    f.append(far)
print("\tcelsius\tfahrenheit")
print("------------------------")
for i in range(len(c)):
    print("\t",c[i],"\t",f[i])
    

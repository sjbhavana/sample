#fibanocci series and position

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
l=list()
i=0
n=int(input("ente the value of n:"))
print("fibanoccii series:")
for i in range(n):
    print(fib(i),end=" ")
    l.append(fib(i))

print("\nindex within the range 0-",n-1)
index=int(input())
print("value=",l[index])

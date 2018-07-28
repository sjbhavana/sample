import random
from random import randint

def rpwd():
    return randint(97,122)
lower=7
upper=12
i=0
pwd=randint(lower,upper)
for i in range(0,pwd):
    r= rpwd()
    r=int(r)
    c=chr(r)
    print(c,end="")
    

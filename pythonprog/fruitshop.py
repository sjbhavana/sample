
class fruit:
    mango=100
    kiwi=100
    e=list()
    def __init__(self,name,salary=2000):
        self.name=name
        self.salary=salary
    def sell(self,item,weight):
        self.item=item
        self.weight=weight
        if(self.item=="mango"):
            fruit.mango-=self.weight
        if(self.item=="kiwi"):
            fruit.kiwi-=self.weight
    def buy(self,item,weight):
        self.item=item
        self.weight=weight
        if(self.item=="mango"):
            fruit.mango+=self.weight
        if(self.item=="kiwi"):
            fruit.kiwi+=self.weight
        


class park:
    two=0
    four=0
    twobill=0
    fourbill=0
    twocost=0
    fourcost=0
    tcount=0
    fcount=0
    e=list()
    n=list()
    def __init__(self,name,salary=3000):
        self.name=name
        self.salary=salary
    def count(self,item,num):
        self.item=item
        self.num=num
        if(self.item=="two"):
            park.two+=1
        if(self.item=="four"):
            park.four+=1
    def bill(self,item,num,hours=1):
        self.item=item
        self.hours=hours
        self.num=num
        if(self.hours==1):
            if(self.item=="two"):
                if self.item in n:
                    park.twocost=park.two*10
                park.twobill+=park.twocost
            if(self.item=="four"):
                if self.item in n:
                    park.fourcost=park.four*20
                park.fourbill+=park.fourcost
        else:
            if(self.item=="two"):
                if self.item in n:
                    park.twocost=park.two*20
                park.twobill+=park.twocost
                
            if(self.item=="four"):
                if self.item in n:
                    park.fourcost=park.four*50
                park.fourbill+=park.fourcost
                
            
        
    


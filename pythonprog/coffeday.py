from datetime import datetime

class ccemply():
    fromypr=0
    frommal=0
    fromindi=0
    fromall3=0

    def __init__(self,fullname,salary,branch):
        self.fullname=fullname
        self.salary=salary
        self.branch=branch
        self.profitfromperson=0
        self.nooftea=0
        self.noofcoffee=0
        self.profitfromcoffee=0
        self.profitfromtea=0
        self.totalbevsold=0

    def sell(self,bev,count):
        if bev=="c":
            self.noofcoffee+=count
            self.profitfromcofee+=count*10
            self.profitfromperson+=count*10
            self.totalbevsold+=count
        if bev=="t":
            self.nooftea+=count
            self.profitfromtea+=count*10
            self.profitfromperson+=count*10
            self.totalbevsold+=count
        
    @classmethod
    def totalfrombranches(cls,branch):
        if branch=="malleshwaram":
            cls.totalfrommal+=xm.profitfromperson
            print(cls.totalfrommal)
        if branch=="yeshwanthpur":
            cls.totalfrommal+=xm.profitfromperson
            print(cls.totalfromypr)
        if branch=="indiranagar":
            cls.totalfrommal+=xm.profitfromperson
            print(cls.totalfromindi)

    @staticmethod
    def printdatetime():
        print(datetime.now())
    def totalfromallbranches():
        ccemply.totalfromall3=ccemply.totalfromaml+ccemply.totalfromypr+ccemply.totalfromindi
        print(ccemply.totalall3)

    class ccdsub(ccemply):
        def __init__(slelf,fullname,salary,branch,doj):
            ccemply.__init__(self,fullname,salary,branch)
            self.doj=doj

            

class employee:
    def __init__(self,first,last,salaray):
        self.first=first
        self.last=last
        self.salaray=salaray
        self.email=first+"-"+last+"@companyname"
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def raise_salary(self):
        self.salaray=self.salaray*3.5
emp1=employee('bhavana','janardhana',100000)
print(emp1.__dict__)
print(emp1.salaray)
print(emp1.first)
print(emp1.email)
print(emp1.fullname())
emp1.raise_salary()
print(emp1.__dict__)

class developer(employee):
    def __init__(self,first,last,salary,language):
        employee.__init__(self,first,last,salary)
        self.language=language

if __name__=='__main__':
    emp3=developer('nakul','nareen',50000,'python')
    print(emp3.__dict__)
    emp3.raise_salary()
    print(emp3.__dict__)
    print(emp3.fullname())
    





























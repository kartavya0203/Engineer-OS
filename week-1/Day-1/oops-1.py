## oops 1 creating a class and an object

class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first +"."+last+"@company.com"   
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1=employee('cory','schafer',50000)
emp2=employee('test','user',60000)

print(emp1.email)
print(emp2.email)
print(emp1.fullname()) ## here the fullnaame method is called using the object so it get passed in the slef instance automatically
print(employee.fullname(emp1)) ## here the fullname method is called using the class name so we have to pass the instance explicitly


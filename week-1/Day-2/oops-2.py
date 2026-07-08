class Employee:

    num_of_emp=0
    raise_amount=1.04 ## class variable raise amount set 

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1 ## this is how we can access the class variable from the instance method and here we donot need the class variable to get overrridden by differnet instances

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def raise_pay(self):
        ## self.pay=int(self.pay*1.04) here we hardcoded the raise_amount so that this can be hard to ind so we make class variable to be it more easier for us
        self.pay=int(self.pay*self.raise_amount) ## the second method to access raise_amount is Employee.raise_amount by the class name

emp1=Employee('John','Doe',50000)
emp2=Employee('Jane','Doe',60000)
print(Employee.num_of_emp) ## this is how we can access the class variable from the class name
print(emp1.pay)
print(emp2.pay)
emp1.raise_pay()  ## we need to call the mehtod to raise the amount
print(emp1.pay)
print(emp1.raise_amount) ## here it access the class that contains the raise amount attribute

print(emp1.__dict__) ## this doesnot conatin the raise amount cause its class

print(Employee.__dict__) ## this contains the raise amountcause its class

Employee.raise_amount=1.05 ## we can change the class variable by
print(Employee.raise_amount)

emp1.raise_amount=1.05
print(emp1.__dict__) # this will contain the raise amount as we changed it for the emp1 instance only and it got added in the dict


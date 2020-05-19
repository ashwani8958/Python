#Exmple for overriding


#Base or parent class
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

#Sub or child class
class SalesOfficer(Employee):
    def __init__(self, name, sal, inc):
        super().__init__(name,sal)
        self.incnt = inc
    #getSalary method is override to calculate incentives
    def getSalary(self):
        print("override")
        return self.salary + self.incnt

e1 = Employee("Rajesh", 9000)
print("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))

s1 = SalesOfficer("Kiran", 10000, 1000)
print("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))

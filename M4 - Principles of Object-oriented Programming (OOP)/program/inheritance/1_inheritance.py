
# inheritance
#parent or base class
class quadrilateral:
    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter = ", p)

    
#sub or child class
class rectangle(quadrilateral):
    #the init method forwards the parameter to the constructor of its base class using
    #the super funtion.The side3 and side4 are made None and oppsite side are made equal
    #by the constructor of the sub class/child class
    def __init__(self,a,b,c=None,d=None):
        super().__init__(a,b,c,d)
        self.side3=self.side1
        self.side4=self.side2

    #parimeter method need not to be define in sub or child class because it will be
    # inheritated by the child class from the parent class
        

"""

>>> q1 = quadrilateral(7,5,6,4)
>>> q1.parimeter()
parimeter = 22

>>> r1 = rectangle(10,20)
>>> r1.perimeter()
parimeter = 60

"""
 

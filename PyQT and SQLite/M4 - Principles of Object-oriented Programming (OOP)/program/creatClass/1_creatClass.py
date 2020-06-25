
#define a class
class person:

    #to see who many object are created from the class, COUNTER variable is created
    #as it is declared before any method it will be accessable to every method
    counter = 0 # it is class attribute, it value is same for all the instances of class.
                # value of the class attributes share by all class object. it is define at class
                # level not inside init method.
    
    #init method is envoked everytime a object is created form the class and is
    # called a constructor. Its jobs is to initialised the atrributes of the object
    def __init__ (self,a,b):
        self.name=a
        self.gender=b
        person.counter = person.counter + 1 #as init method envoked every time, therfore
                                            #counter will increase every time new object got created

    #In python whenever method is created in a class, it is neccessary to pass self
    #self as a argument and that too as a 1st argument
    def showinfo(self):
        print('Name: ', self.name)
        print('Gender: ', self.gender)

    # A method callable by the call not by the individual object are called
    # class method. Add '@classmethod' before every class method and pass 'cls'
    # as the argument instead of 'self' in a class method
    @classmethod
    def ShowCount(cls):
        print("Number of the object created so far: ", cls.counter)

class test:

    count = 0

  
    
    def __init__(self, real = 3):
        self.rt = real

    def get_real(self):
        return self._rt

    def set_real(self, real):
        print("Inside setter")
        self._rt = test.again_real(self, real) # function should be called by the name of class ex test.func_name()        

    def again_real(self, real):
        if test.count < 10:
            return real + 10
        else:
           return real + 100
    
    rt = property(get_real, set_real)

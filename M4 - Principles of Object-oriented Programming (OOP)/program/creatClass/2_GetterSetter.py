""" GETTER and SETTER method are used to control change to variable"""
class car:
    def __init__(self, a = 40):
        self.set_speed(a)# to make initial value also goes from the setter methods

    def get_speed(self):# to get the speed of the car "GETTER METHOD"
        return self._speed

    def set_speed(self,a):# to set the speed of the car to the new value "SETTER METHOD"
        if a < 0 or a > 160:
            print("Speed needs to be in between 0 and 160")
        else:
            self._speed = a
        return

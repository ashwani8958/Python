

class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())

class gift(product):
    def __init__(self,name="Teddy Bear", prc = 500, packing = 100):
        super().__init__(name,prc)
        self.pack = packing

    def get_price(self):
        return self.price + product.deliveryCharge + self.pack
    


"""

class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())

class gift(product):
    wrappingCharge=100
    def __init__(self, nam, prc):
        super().__init__(nam, prc)
    def get_price(self):
        return self.price + product.deliveryCharge + gift.wrappingCharge
"""

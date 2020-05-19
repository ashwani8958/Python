"""Design a ‘book’ class with title, author, publisher, price and author’s royalty as instance variables. Provide getter and setter properties for all variables.
Also define a method royalty() to calculate royalty amount author can expect to receive the following royalties:10% of the retail price on the first 500 copies; 12.5% for the next 1,000 copies sold,
then 15% for all further copies sold.

Then design a new ‘ebook’ class inherited from ‘book’ class. Add ebook format (EPUB, PDF, MOBI etc) as additional instance variable in inherited class.
Override royalty() method to deduct GST @12% on ebooks"""

class book:

    copies = 0 # class attributes
    
    def __init__(self, author = "Ashwani Kumar",publisher = "XYZ", price = 1, royal = 1):
        #instance variable
        self.author = author
        self.publisher = publisher
        self.price = price
        self.royal = royal
        book.copies = book.copies + 1

        
    # Getter and setter method for each instance variable   
    def get_author(self):
        return self._author
    def set_author(self,author):
        self._author = author

    def get_publisher(self):
        return self._publisher
    def set_publisher(self,publisher):
        self._publisher = publisher

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price

    def get_royal(self):
        return self._royal
    def set_royal(self, price):
        self._royal = book.royalty(self, price)
   
    #royalty method for calculating the royalty based on the copies sold 
    def royalty(self, price):
        if book.copies <= 500:
            return price * 0.10
        elif book.copies in range (501, 1000):
            return price * 0.125
        else:
            return price * 0.15

    # making a variable a property 
    author = property(get_author, set_author)
    publisher = property(get_publisher, set_publisher)
    price = property(get_price, set_price)
    royal = property(get_royal, set_royal)

#define sub class
class ebook(book):

    def __init__(self,author = "Ashwani Kumar",publisher = "XYZ", price = 1, royal = 1, format_ebook = "pdf"):
        super().__init__(author, publisher, price, royal)
        self.for_ebook = format_ebook

    
    #overridding the royalty method
    def royalty(self,price):
        self.price = self.price - (self.price * 0.12)
    # Getter and setter method for each instance variable  
    def get_format(self):
        return self._for_ebook
    def set_format(self, format_ebook):
        if format_ebook in ('pdf','epub','mobi'):
            self._for_ebook = format_ebook
        else:
            print("Format Error!!!")

    # making a variable a property
    for_ebook = property(get_format, set_format)


    

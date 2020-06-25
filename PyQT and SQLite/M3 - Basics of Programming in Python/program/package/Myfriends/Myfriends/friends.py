def food(f, num):
    """Takes total and no. of people as argument"""
    tip = 0.1*f #calculates tip
    f = f + tip #add tip to total
    return f/num #return the per person value

def movie(m, num):
    """Take total and no. of the people as arguments"""
    return m/num #returns the per persons value

print("The name attribute is: ", __name__)#check for the name attribute

#Do i have the enough money to splurge on the latest iphone?

def verdict(m1,m2,m3,m4 = 20000):
    total = m1 + m2 + m3
    if total >= m4:
        print("Yes! you can get a new smartphone!")
    else:
        print("Sorry, you can buy the smartphone!")
    return

gift = int(input("Gift money from family: Rs. "))
saving = int(input("saving: Rs. "))
internship = int(input("Money from internship: Rs. "))

verdict(gift,saving,internship,10000)

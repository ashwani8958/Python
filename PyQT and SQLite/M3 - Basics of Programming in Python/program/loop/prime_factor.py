#calculate prime factor

num = int(input("Enter the number "))

d = 2

while num > 1:
    if num%d == 0:
        print(d)
        num = num/d
        continue
    d = d + 1
for char in "INTERNSHALA":     continue

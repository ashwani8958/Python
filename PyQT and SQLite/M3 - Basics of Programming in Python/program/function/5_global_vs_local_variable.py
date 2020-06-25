age = 7
def a():
    print("Global varible 'age': ", globals()['age'])

    #now modifying the GLOBAL varible 'age' INSIDE the function.
    globals()['age']=27
    print("Global variable 'age' modified INSIDE the function: ", globals()['age'])

    #now creating a LOCAL variable, 'age' INSIDE the function.
    age =  11
    print("local variable 'age': ", age)
    return
a()
print("Checking global variable OUTSIDE the function: ", age)

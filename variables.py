# x is global variable because it is declared outside all the functions(i.e myfunc1() and myfunc2())
x = "awesome"
#x can be accessed outside the function , inside the function or any where in the program
print("Python is "+ x)
print(name)
def myfunc1():
    # y is local variable to myfunc1() because it is declared inside the function with name myfunc1()
    y = "Welcome"

    # y can be accessed inside the function myfunc1() only because it is local variable
    print("Manasa "+ y)

myfunc1()

def myfunc2():
    # z is local variable to myfunc2() because z is decalred inside the function myfunc2()
    z = 2
    global name
    name = "priya"
    #z can be accessed inside the function myfunc2() only because it is local variable
    # x is accessed inside the function myfunc2() without declaring inside the function but we can use it because x is global variable
    print("Manasa", x, z)

myfunc2()

print(name)